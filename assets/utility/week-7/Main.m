% x1 = 1;
% y1 = 1.5;
% phi = -45*(pi/180);
x1 = 0;
y1 = 0;
phi = deg2rad(0);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%% SIMULACION VIRTUAL ROBOT %%%%%%%%%%%%%%%%%%%%%%%%%%%%

% a) Configuracion de escena

scene=figure;  % Crear figura (Escena)
sizeScreen=get(0,'ScreenSize'); % Retorna el tamaño de la pantalla del computador
set(scene,'position',sizeScreen); % Congigurar tamaño de la figura
axis equal; % Establece la relación de aspecto para que las unidades de datos sean las mismas en todas las direcciones.
axis([-2 2 -2 2 0 3]); % Ingresar limites minimos y maximos en los ejes x y z [minX maxX minY maxY minZ maxZ]
% view([0 45]); % Orientacion de la figura
grid on; % Mostrar líneas de cuadrícula en los ejes
xlabel('x(m)'); ylabel('y(m)'); zlabel('z(m)'); % Etiqueta de los ejes
camlight right % Luz para la escena

% b) Graficar robots en la posicion inicial
MobileRobot;
scale = 1;
H1=MobilePlot(x1(1),y1(1),phi(1),scale,'b');

