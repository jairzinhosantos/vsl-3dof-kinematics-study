function simulate_differential()
% Movimiento prescrito para verificar v=Jv*qdot, no es control de trayectoria.
root=fileparts(fileparts(fileparts(fileparts(mfilename('fullpath')))));
addpath(fullfile(root,'adapters','matlab','model'));
out=fullfile(root,'outputs','matlab'); if ~exist(out,'dir'),mkdir(out);end
t=(0:0.01:10)'; N=numel(t); L=robot_parameters();
q=[0.3+0.2*sin(0.6*t),0.7+0.15*sin(0.5*t),-0.8+0.1*cos(0.4*t)];
qd=[0.12*cos(0.6*t),0.075*cos(0.5*t),-0.04*sin(0.4*t)];
p=zeros(N,3); v=p; sigma=zeros(N,1);
for k=1:N
    p(k,:)=forward_kinematics(q(k,:),L)'; J=robot_jacobian(q(k,:),L);
    v(k,:)=(J*qd(k,:)')'; s=svd(J); sigma(k)=s(end);
end
vfd=(p(3:end,:)-p(1:end-2,:))/0.02;
err=sqrt(sum((v(2:end-1,:)-vfd).^2,2));
assert(max(err)<1e-5); assert(min(sigma)>1e-3);
writetable(array2table([t,q,qd,p,v,sigma], 'VariableNames', ...
 {'t','q1','q2','q3','dq1','dq2','dq3','x','y','z','vx','vy','vz','sigma_min'}),fullfile(out,'trayectoria.csv'));
f=figure('Color','w');
subplot(2,2,1);plot3(p(:,1),p(:,2),p(:,3),'LineWidth',1.5);axis equal;grid on;xlabel('x (m)');ylabel('y (m)');zlabel('z (m)');
subplot(2,2,2);plot(t,v,'LineWidth',1.2);grid on;xlabel('t (s)');ylabel('v (m/s)');legend('vx','vy','vz');
subplot(2,2,3);semilogy(t(2:end-1),err);grid on;xlabel('t (s)');ylabel('error velocidad (m/s)');
subplot(2,2,4);plot(t,sigma);grid on;xlabel('t (s)');ylabel('sigma min (m/rad)');
print(f,fullfile(out,'simulacion_diferencial.png'),'-dpng','-r180');
fid=fopen(fullfile(out,'simulacion_resumen.txt'),'w'); cleanup=onCleanup(@()fclose(fid));
fprintf(fid,'MATLAB %s\nError max velocidad %.12g m/s\nSigma min %.12g m/rad\n',version,max(err),min(sigma));
end
