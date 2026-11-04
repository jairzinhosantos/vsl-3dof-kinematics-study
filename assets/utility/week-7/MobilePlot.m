function  Mobile_Graph=MobilePlot(x,y,angz,scale,color)
global Uniciclo

% Matriz de rotación z

Rz=[ cos(angz) -sin(angz) 0; sin(angz) cos(angz) 0; 0 0 1];


robotPatch = Rz*Uniciclo.parte1Vertices;
robotPatch(1,:)=robotPatch(1,:)*scale+x;
robotPatch(2,:)=robotPatch(2,:)*scale+y;
robotPatch(3,:)=robotPatch(3,:)*scale;

Mobile_Graph(1) = patch('Faces',Uniciclo.parte1Faces,'Vertices',robotPatch','FaceColor',color,'EdgeColor','none');

robotPatch = Rz*Uniciclo.parte2Vertices;
robotPatch(1,:)=robotPatch(1,:)*scale+x;
robotPatch(2,:)=robotPatch(2,:)*scale+y;
robotPatch(3,:)=robotPatch(3,:)*scale;

Mobile_Graph(2) = patch('Faces',Uniciclo.parte2Faces,'Vertices',robotPatch','FaceColor','k','EdgeColor','none');


robotPatch = Rz*Uniciclo.parte3Vertices;
robotPatch(1,:)=robotPatch(1,:)*scale+x;
robotPatch(2,:)=robotPatch(2,:)*scale+y;
robotPatch(3,:)=robotPatch(3,:)*scale;

Mobile_Graph(3) = patch('Faces',Uniciclo.parte3Faces,'Vertices',robotPatch','FaceColor',[0.8 0.8 0.8],'EdgeColor','none');






