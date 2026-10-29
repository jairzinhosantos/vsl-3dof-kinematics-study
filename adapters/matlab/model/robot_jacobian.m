function [Jv,Jw,Jg] = robot_jacobian(q,L)
% Jacobiano geometrico expresado en base, orden [velocidad lineal; angular].
if nargin < 2, L=robot_parameters(); end
validateattributes(q,{'numeric'},{'real','finite','numel',3});
validateattributes(L,{'numeric'},{'real','finite','positive','numel',3});
q=q(:); L=L(:); c1=cos(q(1)); s1=sin(q(1));
c23=cos(q(2)+q(3)); s23=sin(q(2)+q(3));
rho=L(2)*cos(q(2))+L(3)*c23; h=L(2)*sin(q(2))+L(3)*s23;
Jv=[-s1*rho,-c1*h,-L(3)*c1*s23; ...
     c1*rho,-s1*h,-L(3)*s1*s23; ...
     0,rho,L(3)*c23];
Jw=[0,s1,s1;0,-c1,-c1;1,0,0]; Jg=[Jv;Jw];
end
