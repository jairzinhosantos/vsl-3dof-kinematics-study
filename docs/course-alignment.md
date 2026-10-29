# Course alignment · semanas 4–9

El desarrollo sigue los métodos de clase y utiliza las dimensiones del paper. La carpeta recibida contiene semanas 4 a 9; la semana 10 no está incluida todavía.

| Semana | Material revisado | Aplicación al proyecto |
|---|---|---|
| 4 | MTH, DH y método geométrico; ángulos de Euler | Comparación de posición geométrica, producto de transformaciones y DH |
| 5 | Inversa geométrica, ley de cosenos y dos ramas | Reducción del RRR al plano radial, `atan2` y reconstrucción por directa |
| 6 | Jacobiano analítico/geométrico, derivadas y determinante | Separación de `JL`, `Jw` y Jacobiano completo; comprobación numérica |
| 7 | `Robot_3GDL_CD_Jacobianos.mlx` y apuntes antropomórficos | Misma tabla DH del robot actual; espacio de trabajo y singularidades |
| 8 | Interpoladores cúbico y quíntico | Posición, velocidad y aceleración articulares con condiciones de frontera |
| 9 | Control de posición y de seguimiento | Pseudoinversa, error cartesiano e integración de Euler; adaptación de 4 a 3 GDL |

Los originales están en [assets/utility](../assets/utility/README.md), conservados sin editar. Se inspeccionaron los scripts de los archivos MLX/ZIP sin ejecutarlos en MATLAB y se contrastaron las ecuaciones manuscritas con los programas.

## Correspondencia de notación

| Clase | Código y documento |
|---|---|
| `theta1`, `theta2`, `theta3` | `q[0]`, `q[1]`, `q[2]`, en radianes |
| `DHL(theta,d,a,alpha)` | `dh(theta,d,a,alpha)`, todos los ángulos en radianes |
| `M03` | Matriz homogénea `forward(q)[0]` |
| `Pos = M03(1:3,4)` | `P03 = M03[:3,3]` |
| `JL = jacobian(Pos,theta)` | `jacobian(q)[0]`; antes denominado `Jv` |
| `Jw = [z0 z1 z2]` | `jacobian(q)[1]` |
| `J = [JL; Jw]` | `jacobian(q)[2]`, orden `[v; omega]` |
| `he = hd-h` | Error de posición `desired-p` |
| `qpRef = pinv(J)*(hdp+K*he)` | Control con `JL`, seguido de `q[k+1]=q[k]+dt*dq[k]` |

`J_a` relaciona derivadas de una parametrización de pose; `J=[JL;Jw]` relaciona velocidad lineal y angular. No se identifica la velocidad angular con derivadas de Euler. En el script de semana 7, `Det_Ja` contiene `det(JL)`, no el determinante de una matriz 6×3.

## Adaptaciones necesarias

- Las semanas 4–6 incluyen un SCARA RRP. Su desplazamiento prismático y sus signos no se trasladan al robot RRR.
- La semana 7 usa la misma estructura DH, pero otras longitudes y rangos ilustrativos. Se conservan las dimensiones del paper: 0.04, 0.29 y 0.24 m. Los rangos de muestreo del curso no se presentan como límites mecánicos del VSL.
- La función MATLAB combina `cos/sin` con `rotx(alpha)` en grados. Python utiliza radianes para todos los ángulos; `90°` se convierte en `pi/2`.
- En la inversa se descuenta la altura: `z = pz-l1`. Se utiliza `atan2` para preservar cuadrantes. El ángulo articular del codo es cero con eslabones extendidos; por ello `cos(q3)=(r²+z²-l2²-l3²)/(2*l2*l3)`. Se distingue del ángulo interior suplementario del triángulo. Las expresiones manuscritas se verifican por reconstrucción, no por copia literal.
- Los controles de semana 9 utilizan cuatro articulaciones. Se adapta la ley a las tres del paper; no se copian sus dimensiones ni sus mallas como si fueran el VSL.

## Comprobaciones disponibles

[Resultados preparados](../simulations/course/README.md): tres métodos de directa, dos ramas de inversa, 9261 posiciones muestreadas, interpoladores, control de posición, seguimiento y un caso de estancamiento singular. Las 29 pruebas comprueban además Jacobianos lineal/angular, determinante simbólico y convergencia temporal.

El modelo base anterior era compatible con la semana 7. Faltaban la exposición por métodos, la inversa, los interpoladores y el control ejecutado; se incorporan en esta versión para revisión.

## Falta por contrastar

Material de semana 10; límites mecánicos documentados del robot; discrepancias de la tabla 3 del paper; aportes y revisión del equipo. La nota de semana 7 menciona también dinámica en un caso de estudio, mientras la consigna del parcial se ha organizado en cinco bloques cinemáticos. Su aplicación a esta entrega se resolverá internamente. No se implementa ni se afirma validación dinámica o física.
