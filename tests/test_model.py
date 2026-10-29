import numpy as np
import pytest
from robotics_study.model import forward, jacobian, joint_points, DEFAULT_LENGTHS
from robotics_study.simulation import simulate

@pytest.mark.parametrize('seed',[2026,42])
def test_jacobians_against_independent_dh_and_finite_difference(seed):
    for q in np.random.default_rng(seed).uniform(-np.pi,np.pi,(100,3)):
        T,O,Z=forward(q); R=T[:3,:3]; p=T[:3,3]; J,W,_=jacobian(q)
        np.testing.assert_allclose(R.T@R,np.eye(3),atol=1e-12)
        assert np.linalg.det(R)==pytest.approx(1)
        np.testing.assert_allclose(J,np.column_stack([np.cross(Z[:,i],p-O[:,i]) for i in range(3)]),atol=1e-12)
        for i in range(3):
            delta=np.eye(3)[i]*1e-6; Tp=forward(q+delta)[0]; Tm=forward(q-delta)[0]
            np.testing.assert_allclose(J[:,i],(Tp[:3,3]-Tm[:3,3])/2e-6,atol=1e-8)
            S=((Tp[:3,:3]-Tm[:3,:3])/2e-6)@R.T
            np.testing.assert_allclose(W[:,i],[S[2,1],S[0,2],S[1,0]],atol=1e-8)
        rho=DEFAULT_LENGTHS[1]*np.cos(q[1])+DEFAULT_LENGTHS[2]*np.cos(q[1]+q[2])
        assert np.linalg.det(J)==pytest.approx(-DEFAULT_LENGTHS[1]*DEFAULT_LENGTHS[2]*rho*np.sin(q[2]),abs=1e-12)

@pytest.mark.parametrize('q,expected',[([0,0,0],2),([0,np.pi/2,0],1),([.4,.7,-.9],3)])
def test_position_and_full_jacobian_have_different_rank(q,expected):
    J,_,G=jacobian(q)
    assert np.linalg.matrix_rank(J,tol=1e-10)==expected
    assert np.linalg.matrix_rank(G,tol=1e-10)==3

def test_base_axis_singularity_without_straight_elbow():
    q3=np.pi/3; l2,l3=DEFAULT_LENGTHS[1:]
    q2=np.arctan2(l2+l3*np.cos(q3),l3*np.sin(q3))
    assert np.linalg.matrix_rank(jacobian([0,q2,q3])[0],tol=1e-10)==2

def test_units_and_zero_configuration():
    points=joint_points([0,0,0])
    np.testing.assert_allclose(points,[[0,0,0],[0,0,.04],[.29,0,.04],[.53,0,.04]],atol=1e-12)
    np.testing.assert_allclose(np.linalg.norm(np.diff(points,axis=0),axis=1),DEFAULT_LENGTHS)

@pytest.mark.parametrize('q',[[0,0],[0,float('nan'),0],[[0],[0],[0]]])
def test_reject_invalid_angles(q):
    with pytest.raises(ValueError):forward(q)

def test_reject_invalid_length():
    with pytest.raises(ValueError):jacobian([0,0,0],[.04,-.29,.24])

def test_velocity_convergence():
    errors=[simulate(dt=dt)['error'].max() for dt in [.02,.01,.005]]
    assert errors[0]<1e-5
    assert 3.9<errors[0]/errors[1]<4.1
    assert 3.9<errors[1]/errors[2]<4.1

@pytest.mark.parametrize('duration,dt',[(0,0),(1,-1),(1,.3),(float('nan'),.1)])
def test_reject_invalid_time_grid(duration,dt):
    with pytest.raises(ValueError):simulate(duration,dt)

def test_symbolic_derivative():
    import sympy as s
    q1,q2,q3,l1,l2,l3=s.symbols('q1 q2 q3 l1 l2 l3',real=True)
    rho=l2*s.cos(q2)+l3*s.cos(q2+q3);h=l2*s.sin(q2)+l3*s.sin(q2+q3)
    p=s.Matrix([s.cos(q1)*rho,s.sin(q1)*rho,l1+h])
    J=p.jacobian([q1,q2,q3])
    assert s.trigsimp(J.det()+l2*l3*rho*s.sin(q3))==0
