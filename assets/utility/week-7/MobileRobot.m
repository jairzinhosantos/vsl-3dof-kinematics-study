function  MobileRobot

parte1 = stlRead('parte1.stl'); % Exportar stl en metros y formato binario
parte2 = stlRead('parte2.stl'); % Exportar stl en metros y formato binario
parte3 = stlRead('parte3.stl'); % Exportar stl en metros y formato binario

global Uniciclo;


Uniciclo.parte1Vertices=parte1.vertices';
Uniciclo.parte1Faces=parte1.faces;

Uniciclo.parte2Vertices=parte2.vertices';
Uniciclo.parte2Faces=parte2.faces;

Uniciclo.parte3Vertices=parte3.vertices';
Uniciclo.parte3Faces=parte3.faces;


