function [p,T,origenes,ejes] = forward_kinematics(q,L)
% DH estandar: Rz(theta)*Tz(d)*Tx(a)*Rx(alpha). Angulos en radianes.
if nargin < 2, L = robot_parameters(); end
validateattributes(q,{'numeric'},{'real','finite','numel',3});
validateattributes(L,{'numeric'},{'real','finite','positive','numel',3});
q=q(:); L=L(:); a=[0;L(2);L(3)]; d=[L(1);0;0]; alpha=[pi/2;0;0];
T=eye(4); origenes=zeros(3,4); ejes=zeros(3,3);
for i=1:3
    origenes(:,i)=T(1:3,4); ejes(:,i)=T(1:3,3);
    c=cos(q(i)); s=sin(q(i)); ca=cos(alpha(i)); sa=sin(alpha(i));
    A=[c,-s*ca,s*sa,a(i)*c; s,c*ca,-c*sa,a(i)*s; ...
       0,sa,ca,d(i); 0,0,0,1];
    T=T*A;
end
p=T(1:3,4); origenes(:,4)=p;
end
