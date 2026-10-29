"""Modelo rígido nominal. Geometría: Ramzy et al. (2024), tablas 1 y 2."""
import numpy as np

DEFAULT_LENGTHS = np.array([0.04, 0.29, 0.24])
DEFAULT_LENGTHS.setflags(write=False)

def vector3(value, name):
    value = np.asarray(value, dtype=float)
    if value.shape != (3,) or not np.isfinite(value).all():
        raise ValueError(f'{name} debe tener forma (3,) y valores finitos')
    return value

def parameters(q, lengths):
    q = vector3(q, 'q'); lengths = vector3(lengths, 'lengths')
    if np.any(lengths <= 0):
        raise ValueError('Las longitudes deben ser positivas')
    return q, lengths

def dh(theta, a, d, alpha):
    """DH estándar: Rz(theta) Tz(d) Tx(a) Rx(alpha)."""
    c, s, ca, sa = np.cos(theta), np.sin(theta), np.cos(alpha), np.sin(alpha)
    return np.array([[c,-s*ca,s*sa,a*c], [s,c*ca,-c*sa,a*s],
                     [0,sa,ca,d], [0,0,0,1.]])

def forward(q, lengths=DEFAULT_LENGTHS):
    """Devuelve T_03, orígenes previos y ejes previos, expresados en base."""
    q, lengths = parameters(q, lengths)
    transform = np.eye(4); origins = []; axes = []
    for theta,a,d,alpha in zip(q,[0,*lengths[1:]],[lengths[0],0,0],[np.pi/2,0,0]):
        origins.append(transform[:3,3].copy()); axes.append(transform[:3,2].copy())
        transform = transform @ dh(theta,a,d,alpha)
    return transform, np.array(origins).T, np.array(axes).T

def joint_points(q, lengths=DEFAULT_LENGTHS):
    """Base, hombro, codo y efector, matriz (4,3), metros."""
    transform, origins, _ = forward(q, lengths)
    return np.vstack([origins.T, transform[:3,3]])

def jacobian(q, lengths=DEFAULT_LENGTHS):
    """Jv (m/rad), Jw y Jg=[Jv;Jw], expresados en base."""
    q, lengths = parameters(q, lengths)
    c,s = np.cos(q[0]),np.sin(q[0]); c23,s23 = np.cos(q[1]+q[2]),np.sin(q[1]+q[2])
    rho = lengths[1]*np.cos(q[1])+lengths[2]*c23
    h = lengths[1]*np.sin(q[1])+lengths[2]*s23
    linear = np.array([[-s*rho,-c*h,-lengths[2]*c*s23],
                       [c*rho,-s*h,-lengths[2]*s*s23],[0,rho,lengths[2]*c23]])
    angular = np.array([[0,s,s],[0,-c,-c],[1,0,0]])
    return linear, angular, np.vstack([linear,angular])
