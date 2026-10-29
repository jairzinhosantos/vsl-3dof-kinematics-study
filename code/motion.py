"""Movimiento articular prescrito; no implementa control en lazo cerrado."""
import numpy as np
from model import forward, jacobian, joint_points, DEFAULT_LENGTHS

def prescribed_motion(t):
    t = np.asarray(t)
    q = np.column_stack([.3+.2*np.sin(.6*t), .7+.15*np.sin(.5*t), -.8+.1*np.cos(.4*t)])
    dq = np.column_stack([.12*np.cos(.6*t), .075*np.cos(.5*t), -.04*np.sin(.4*t)])
    return q, dq

def simulate(duration=10., dt=.01, lengths=DEFAULT_LENGTHS):
    if not np.isfinite([duration,dt]).all() or dt<=0 or duration<2*dt:
        raise ValueError('Se requieren duration >= 2*dt y dt positivo')
    steps = round(duration/dt)
    if not np.isclose(steps*dt,duration):
        raise ValueError('duration debe ser múltiplo de dt')
    t = np.arange(steps+1)*dt; q,dq = prescribed_motion(t)
    points = np.array([joint_points(row,lengths) for row in q])
    p = points[:,-1,:]
    v = np.array([jacobian(row,lengths)[0]@rate for row,rate in zip(q,dq)])
    sigma = np.array([np.linalg.svd(jacobian(row,lengths)[0],compute_uv=False)[-1] for row in q])
    error = np.linalg.norm(v[1:-1]-(p[2:]-p[:-2])/(2*dt),axis=1)
    return dict(t=t,q=q,dq=dq,points=points,p=p,v=v,sigma=sigma,error=error)
