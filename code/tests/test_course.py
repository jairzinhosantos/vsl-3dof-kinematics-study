import numpy as np
import pytest
from course import geometric_position, homogeneous, inverse_position, polynomial, control, cartesian_reference
from model import forward, dh


def test_course_dh_argument_order_and_units():
    np.testing.assert_allclose(dh(0,.04,0,np.pi/2),[[1,0,0,0],[0,0,-1,0],[0,1,0,.04],[0,0,0,1]],atol=1e-15)


def test_three_forward_methods_and_four_inverse_branches():
    # XYZ con precisión completa del caso regular de la diapositiva 24.
    target = [0.33341978045700893, 0.19249999999999998, 0.2911473670974872]
    expected = [[30, 6.23529807, 60], [30, 60, -60],
                [-150, 120, 60], [-150, 173.76470193, -60]]
    np.testing.assert_allclose(np.rad2deg(inverse_position(target)), expected, rtol=0, atol=1e-7)
    for q in np.random.default_rng(2026).uniform(-2.5,2.5,(120,3)):
        transform=forward(q)[0]
        np.testing.assert_allclose(homogeneous(q),transform,atol=1e-14)
        np.testing.assert_allclose(geometric_position(q),transform[:3,3],atol=1e-14)
        solutions=inverse_position(transform[:3,3])
        assert len(solutions) == 4
        assert len(np.unique(solutions.round(10), axis=0)) == 4
        assert any(np.allclose(np.sin((candidate-q)/2), 0, atol=1e-10) for candidate in solutions)
        for solution in solutions:
            np.testing.assert_allclose(geometric_position(solution), transform[:3,3], atol=1e-12, rtol=0)
            np.testing.assert_allclose(forward(solution)[0][:3,3], transform[:3,3], atol=1e-12, rtol=0)


def test_inverse_degenerate_and_unreachable_cases():
    assert len(inverse_position([1,0,.04]))==0
    assert len(inverse_position([0,0,.04]))==0  # l2 != l3: hueco interior
    for radius in [.05, .53]:
        target = [radius, 0, .04]
        solutions = inverse_position(target)
        assert len(solutions) == 2
        for candidate in solutions:
            np.testing.assert_allclose(geometric_position(candidate), target, atol=1e-12)
    assert len(inverse_position([0,0,.30])) == 2
    assert len(inverse_position([0,0,.57])) == 1
    assert len(inverse_position([0,0,.04],[.04,.2,.2])) == 1
    for q in inverse_position([0,0,.30],base_angle=.7):
        assert q[0]==pytest.approx(.7)
        np.testing.assert_allclose(forward(q)[0][:3,3],[0,0,.30],atol=1e-12)
    for q in inverse_position([0,0,.04],[.04,.2,.2]):
        np.testing.assert_allclose(forward(q,[.04,.2,.2])[0][:3,3],[0,0,.04],atol=1e-12)

@pytest.mark.parametrize('order',[3,5])
def test_interpolation_boundaries_and_derivatives(order):
    q0=np.array([.2,.5,-.8]);qf=np.array([-.3,.2,-1.1]);T=3.
    q,v,a=polynomial(q0,qf,np.array([0.,T]),T,order)
    np.testing.assert_allclose(q,[q0,qf],atol=1e-14);np.testing.assert_allclose(v,0,atol=1e-14)
    if order==5:np.testing.assert_allclose(a,0,atol=1e-14)
    h=1e-5;t=1.1
    qp,vp,_=polynomial(q0,qf,t+h,T,order);qm,vm,_=polynomial(q0,qf,t-h,T,order)
    _,v,a=polynomial(q0,qf,t,T,order)
    np.testing.assert_allclose((qp-qm)/(2*h),v,atol=1e-9)
    np.testing.assert_allclose((vp-vm)/(2*h),a,atol=1e-9)


def test_reference_velocity_and_position_control():
    t=1.;h=1e-5
    np.testing.assert_allclose((cartesian_reference(t+h)[0]-cartesian_reference(t-h)[0])/(2*h),cartesian_reference(t)[1],atol=1e-10)
    target=geometric_position([-.3,.8,-1.])
    result=control([.5,.6,-.8],target=target)
    assert np.linalg.norm(result['error'][-1])<2e-5
    assert result['sigma'].min()>.01
    np.testing.assert_allclose(np.diff(result['q'],axis=0),.1*result['dq'],atol=1e-14)


def test_tracking_converges_under_step_refinement():
    q0=inverse_position(cartesian_reference(0.)[0])[1]+[.12,-.08,.10]
    errors=[]
    for dt in [.1,.05]:
        r=control(q0,duration=20,dt=dt)
        assert r['sigma'].min()>.01
        errors.append(np.sqrt(np.mean(np.sum(r['error'][r['t']>=10]**2,axis=1))))
    assert errors[1]<.6*errors[0]


def test_pseudoinverse_does_not_solve_unavailable_singular_direction():
    r=control([0,0,0],target=[.50,0,.04],duration=1)
    assert np.linalg.norm(r['error'][-1])==pytest.approx(.03)
    np.testing.assert_allclose(r['q'],0,atol=1e-12)

@pytest.mark.parametrize('args',[(0,.1,1),(1,0,1),(1,.3,1),(1,.1,-1)])
def test_control_rejects_invalid_parameters(args):
    with pytest.raises(ValueError):control([0,0,0],duration=args[0],dt=args[1],gain=args[2])
