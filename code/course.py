"""Métodos de las semanas 4–9 adaptados al robot RRR del paper."""
import numpy as np
from model import DEFAULT_LENGTHS, parameters, vector3, forward, jacobian


def geometric_position(q, lengths=DEFAULT_LENGTHS):
    q, (l1,l2,l3) = parameters(q,lengths)
    r = l2*np.cos(q[1])+l3*np.cos(q[1]+q[2])
    return np.array([r*np.cos(q[0]),r*np.sin(q[0]),l1+l2*np.sin(q[1])+l3*np.sin(q[1]+q[2])])


def homogeneous(q, lengths=DEFAULT_LENGTHS):
    """Producto de rotaciones y traslaciones, independiente de la función DH."""
    q, (l1,l2,l3) = parameters(q,lengths)
    def rz(t):
        c,s=np.cos(t),np.sin(t)
        return np.array([[c,-s,0,0],[s,c,0,0],[0,0,1,0],[0,0,0,1.]])
    def shift(x,y,z):
        t=np.eye(4);t[:3,3]=[x,y,z];return t
    rx90=np.array([[1,0,0,0],[0,0,-1,0],[0,1,0,0],[0,0,0,1.]])
    return rz(q[0])@shift(0,0,l1)@rx90@rz(q[1])@shift(l2,0,0)@rz(q[2])@shift(l3,0,0)


def inverse_position(position, lengths=DEFAULT_LENGTHS, base_angle=0., tol=1e-10):
    """Soluciones XYZ en radianes, primero radio positivo y luego negativo.

    Cada base devuelve el codo positivo antes del negativo. En el eje se usa
    base_angle como representante. Un objetivo inalcanzable devuelve (0, 3).
    """
    (x, y, z), (l1, l2, l3) = parameters(position, lengths)
    if not np.isfinite(base_angle):
        raise ValueError("base_angle debe ser finito")
    radius = np.hypot(x, y)
    height = z - l1
    c3 = (radius**2 + height**2 - l2**2 - l3**2) / (2*l2*l3)
    if abs(c3) > 1 + tol:
        return np.empty((0, 3))
    if abs(abs(c3) - 1) <= 8*np.finfo(float).eps:
        c3 = np.sign(c3)
    c3 = np.clip(c3, -1, 1)

    # En el centro, dos eslabones iguales plegados permiten cualquier hombro.
    if radius <= tol and abs(height) <= tol and abs(l2 - l3) <= tol:
        return np.array([[base_angle, 0., np.pi]])
    if radius <= tol:
        bases = [(base_angle, 0.)]
    else:
        angle = np.arctan2(y, x)
        bases = [(angle, radius), (angle + np.pi, -radius)]

    elbow = np.arccos(c3)
    elbows = [elbow] if abs(c3) == 1 else [elbow, -elbow]
    solutions = []
    for q1, signed_radius in bases:
        for q3 in elbows:
            offset = np.arctan2(l3*np.sin(q3), l2 + l3*c3)
            q2 = np.arctan2(height, signed_radius) - offset
            solutions.append([q1, q2, q3])
    return (np.array(solutions) + np.pi) % (2*np.pi) - np.pi


def polynomial(q0,qf,t,duration,order=5):
    """Interpolación articular en rad; velocidad inicial/final nula; orden 5: aceleración nula."""
    q0=vector3(q0,'q0');qf=vector3(qf,'qf');t=np.asarray(t,dtype=float)
    if not np.isfinite(duration) or duration<=0 or not np.isfinite(t).all() or np.any(t<0) or np.any(t>duration):
        raise ValueError('Tiempo fuera del intervalo [0,duration]')
    u=t/duration
    if order==3:
        s=3*u**2-2*u**3;ds=(6*u-6*u**2)/duration;dds=(6-12*u)/duration**2
    elif order==5:
        s=10*u**3-15*u**4+6*u**5;ds=(30*u**2-60*u**3+30*u**4)/duration;dds=(60*u-180*u**2+120*u**3)/duration**2
    else:raise ValueError('El orden debe ser 3 o 5')
    delta=qf-q0
    return q0+s[...,None]*delta,ds[...,None]*delta,dds[...,None]*delta


def cartesian_reference(t):
    """Trayectoria pequeña elegida para el RRR, con la forma sinusoidal de semana 9."""
    t=np.asarray(t)
    p=np.stack([.35+.03*np.cos(.4*t),.10+.03*np.sin(.4*t),.23+.02*np.sin(.5*t)],axis=-1)
    v=np.stack([-.012*np.sin(.4*t),.012*np.cos(.4*t),.01*np.cos(.5*t)],axis=-1)
    return p,v


def control(q0,duration=10.,dt=.1,gain=1.,target=None,lengths=DEFAULT_LENGTHS):
    """qdot=pinv(JL)*(hdot+K*(hd-h)); Euler explícito. Sin saturación ni dinámica."""
    q0,lengths=parameters(q0,lengths)
    if not np.isfinite([duration,dt,gain]).all() or dt<=0 or duration<dt or gain<=0:
        raise ValueError('Duración, paso y ganancia deben ser positivos')
    steps=round(duration/dt)
    if not np.isclose(steps*dt,duration):raise ValueError('duration debe ser múltiplo de dt')
    t=np.arange(steps+1)*dt
    if target is None:desired,velocity=cartesian_reference(t)
    else:desired=np.tile(vector3(target,'target'),(steps+1,1));velocity=np.zeros_like(desired)
    q=np.empty((steps+1,3));q[0]=q0;p=np.empty_like(q);dq=np.empty((steps,3));sigma=np.empty(steps+1)
    for k in range(steps+1):
        p[k]=forward(q[k],lengths)[0][:3,3];JL=jacobian(q[k],lengths)[0]
        sigma[k]=np.linalg.svd(JL,compute_uv=False)[-1]
        if k<steps:
            dq[k]=np.linalg.pinv(JL)@(velocity[k]+gain*(desired[k]-p[k]))
            q[k+1]=q[k]+dt*dq[k]
    error=desired-p
    return dict(t=t,q=q,p=p,desired=desired,dq=dq,error=error,sigma=sigma)
