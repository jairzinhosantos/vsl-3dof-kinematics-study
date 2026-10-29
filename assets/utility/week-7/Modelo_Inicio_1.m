clear
close all
clc

%%%%%%%%%%%%%%%%%%%%%%%TIEMPO %%%%%%%%%%%%%%%%%%%%
tf = 70;
ts = 0.1;
t = 0 :  ts : tf;
N = length(t);

%%%%%%%%%%%%%%%%%%%% PARÁMETROS_DEL_ROBOT %%%%%%%%
a = 0.2;

%%%%%%%%%%%%%%%%%%%% CONDICIONES_INICIALES %%%%%%%%
x1 = zeros(1,N+1);
y1 = zeros(1,N+1);

x1(1) = 1;
y1(1) = -1;

%%%%%%%%%%%%%%%%%%%% MODELO_GEOMÉTRICO %%%%%%%%%%%%

hx = zeros(1,N+1);
hy = zeros(1,N+1);
phi = zeros(1,N+1);

phi(1) = 0;

hx(1) = x1(1) + a*cos(phi(1));
hy(1) = y1(1) + a*sin(phi(1));

%%%%%%%%%%%%%%%%% VELOCIDADES_DE_REFERENCIA %%%%%%%%%
uRef = 0.2*ones(1,N);
wRef = 0.2*ones(1,N);

%%%%%%%%%%%%%%%%%%% BUCLE %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
for k = 1 : N
    phi(k+1) = phi(k) + wRef(k)*ts;

    xp1 = uRef(k)*cos(phi(k+1));
    yp1 = uRef(k)*sin(phi(k+1));

    x1(k+1) = x1(k) + xp1*ts;
    y1(k+1) = y1(k) + yp1*ts;

    hx(k+1) = x1(k+1) + a*cos(phi(k+1));
    hy(k+1) = y1(k+1) + a*sin(phi(k+1));
end

%%%%%%%%%%%%% SIMULACIÓN_VIRTUAL_ROBOT %%%%%%%%%%%

% a) Confifuración_escena

scena = figure;
sizeScreem = get(0,'ScreenSize');
set(scena,'position',sizeScreem);
axis equal
axis([-10 10 -10 10 0 3]);
grid on;
xlabel('x(m)');
camlight right

% b) Graficar_robot_posición_inicial

MobileRobot;
scale = 1;
H1 = MobilePlot(x1(1),y1(1),phi(1),scale,'b');
hold on

% c) Graficar_trayectorias

H2 = plot(hx(1),hy(1),'k','lineWidth',2);

% d) Pasos_simulación

step = 20;
for k = 1:step:N
    
    delete(H1);
    delete(H2);
    
    H1 = MobilePlot(x1(k),y1(k),phi(k),scale,'b');
    H2 = plot(hx(1:k),hy(1:k),'k','lineWidth',2);
    
    pause(ts);
end
