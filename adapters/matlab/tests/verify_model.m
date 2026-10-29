function verify_model()
% Ejecutar desde cualquier directorio. No requiere toolboxes.
root=fileparts(fileparts(fileparts(fileparts(mfilename('fullpath')))));
addpath(fullfile(root,'adapters','matlab','model'));
out=fullfile(root,'outputs','matlab'); if ~exist(out,'dir'),mkdir(out);end
diary(fullfile(out,'verificacion.txt')); cleanup=onCleanup(@()diary('off'));
rng(2026); L=robot_parameters(); epsq=1e-6; maxerr=zeros(1,5);
for k=1:200
    q=(2*rand(3,1)-1)*pi; [p,T,O,Z]=forward_kinematics(q,L);
    [Jv,Jw]=robot_jacobian(q,L); Jfd=zeros(3); Wfd=zeros(3); Jcross=zeros(3);
    for i=1:3
        dq=zeros(3,1); dq(i)=epsq;
        [pp,Tp]=forward_kinematics(q+dq,L); [pm,Tm]=forward_kinematics(q-dq,L);
        Jfd(:,i)=(pp-pm)/(2*epsq); Jcross(:,i)=cross(Z(:,i),p-O(:,i));
        S=((Tp(1:3,1:3)-Tm(1:3,1:3))/(2*epsq))*T(1:3,1:3)';
        Wfd(:,i)=[S(3,2);S(1,3);S(2,1)];
    end
    rho=L(2)*cos(q(2))+L(3)*cos(q(2)+q(3));
    pclosed=[cos(q(1))*rho;sin(q(1))*rho;L(1)+L(2)*sin(q(2))+L(3)*sin(q(2)+q(3))];
    err=[norm(Jv-Jfd,'fro'),norm(Jv-Jcross,'fro'),norm(Jw-Wfd,'fro'), ...
         abs(det(Jv)+L(2)*L(3)*rho*sin(q(3))),norm(p-pclosed)];
    maxerr=max(maxerr,err);
    assert(norm(T(1:3,1:3)'*T(1:3,1:3)-eye(3),'fro')<1e-12);
    assert(abs(det(T(1:3,1:3))-1)<1e-12);
end
assert(all(maxerr<[1e-8,1e-12,1e-8,1e-12,1e-12]));
[Jv,~,Jg]=robot_jacobian([0;0;0],L); assert(rank(Jv,1e-10)==2); assert(rank(Jg,1e-10)==3);
% Singularidad de eje de base, con sin(q3) distinto de cero.
q3=pi/3; q2=atan2(L(2)+L(3)*cos(q3),L(3)*sin(q3));
[Jv,~,~]=robot_jacobian([0;q2;q3],L); assert(rank(Jv,1e-10)==2);
[Jv,~,~]=robot_jacobian([0;pi/2;0],L); assert(rank(Jv,1e-10)==1);
fprintf('MATLAB %s | 200 configuraciones | semilla 2026\n',version);
fprintf('Maximos [Jfd Jgeometrico Jwfd determinante posicion]:\n'); disp(maxerr);
fprintf('Pruebas numericas aprobadas; resultado pendiente de revision humana.\n');
end
