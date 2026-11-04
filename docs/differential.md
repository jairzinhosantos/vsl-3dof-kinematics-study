# Differential kinematics

Nota de estudio del desarrollo incluido en el [borrador del informe](../report/output/report.pdf), preparado para revisión. Se emplea la notación de las semanas 6 y 7: `JL`, `Jw` y `J=[JL;Jw]`; véase la [correspondencia con las clases](course-alignment.md).

La [guía paso a paso](../notebooks/differential-kinematics/README.md) desarrolla los fundamentos y enlaza el notebook ejecutado.

## Pregunta y fundamento

¿Cómo se relacionan las velocidades de las tres articulaciones con la velocidad lineal y angular del efector? Se parte del [modelo común](model.md), derivado de la tabla DH y ecuaciones (6)-(8) del [paper](paper.md). El concepto de Jacobiano se apoya en [Modern Robotics, capítulo 5](https://modernrobotics.northwestern.edu/nu-gm-book-resource/velocity-kinematics-and-statics/).

## Jacobiano de posición

Se define c1=cos(q1), s1=sin(q1), c23=cos(q2+q3), s23=sin(q2+q3). La regla de la cadena da:

$$\dot p=\frac{\partial p}{\partial q}\dot q=J_L(q)\dot q.$$

Las derivadas auxiliares son d(rho)/dq2=-h, d(rho)/dq3=-l3 s23, dh/dq2=rho y dh/dq3=l3 c23. Por tanto:

$$J_L=\begin{bmatrix}-s_1\rho&-c_1h&-l_3c_1s_{23}\\c_1\rho&-s_1h&-l_3s_1s_{23}\\0&\rho&l_3c_{23}\end{bmatrix}.$$

Cada columna es la velocidad del efector causada por velocidad unitaria en esa articulación. JL tiene unidades m/rad; al multiplicar por rad/s se obtiene m/s. l1 no aparece porque es un desplazamiento constante, aunque sí interviene en posición e inversa.

## Construcción geométrica independiente

Para una articulación rotacional:

$$J_{v,i}=z_{i-1}\times(p-o_{i-1}).$$

En la base, z0=[0,0,1]ᵀ; z1=z2=[s1,-c1,0]ᵀ; o0=0; o1=[0,0,l1]ᵀ y o2=[l2 c1 cos(q2), l2 s1 cos(q2), l1+l2 sin(q2)]ᵀ. Los productos cruzados recuperan las tres columnas anteriores. Esta comparación se ejecuta sobre la cadena DH en los tests, evitando comprobar la fórmula únicamente contra una copia de sí misma.

## Velocidad angular

$$\omega=J_\omega\dot q,\qquad J_\omega=\begin{bmatrix}0&s_1&s_1\\0&-c_1&-c_1\\1&0&0\end{bmatrix}.$$

$$\begin{bmatrix}\dot p\\\omega\end{bmatrix}=\underbrace{\begin{bmatrix}J_L\\J_\omega\end{bmatrix}}_{J_g\in\mathbb R^{6\times3}}\dot q.$$

El orden es `[v;omega]` y ambas velocidades están expresadas en la base. La velocidad angular no es, en general, la derivada de ángulos de Euler. Se comprueba con la matriz antisimétrica `Rdot R.T`. Este Jacobiano de velocidad del punto final no debe confundirse automáticamente con un Jacobiano espacial de tornillos.

Tres entradas articulares no permiten imponer seis componentes independientes de pose. La tarea de control implementada es de posición.

## Ejemplo

q=[30,40,-50] grados y qdot=[0.10,-0.20,0.15] rad/s producen aproximadamente:

- p=[0.397078,0.229253,0.184733] m.
- v=[0.007557,0.057307,-0.056248] m/s.
- omega=[-0.025000,0.043301,0.100000] rad/s.
- det(JL)=0.0244461; condición 2 de JL≈5.22485.

El ejemplo es un ensayo numérico elegido por el equipo, no una medición ni una configuración prescrita por el fabricante.

## Relación con singularidades y control

La factorización del determinante es:

$$\det J_L=-l_2l_3\rho\sin q_3.$$

Las singularidades de posición aparecen con rho=0 o sin(q3)=0. En q=0 el rango de JL es 2; en q=[0,pi/2,0] es 1. No implica pérdida del rango máximo de Jg. Para l2>0, si Jg u=0, la parte angular exige u1=0 y u2=-u3; la lineal restante tiene norma |u2|l2, por lo que u=0 y Jg tiene rango 3.

El control de seguimiento implementado utiliza:

$$\dot q=J_L^\dagger(\dot p_d+K(p_d-p)).$$

Fuera de singularidades y con ejecución ideal, edot=-Ke. Cerca de singularidades puede estudiarse la inversa amortiguada `JL.T @ inv(JL @ JL.T + lambda² I)`, con unidades compatibles. No elimina la necesidad de límites ni el análisis discreto. El [caso de curso](../simulations/course/README.md) implementa la pseudoinversa y Euler explícito, e incluye un ensayo singular donde el error no disminuye.

## Evidencia y límites

[El caso diferencial](../simulations/differential/README.md) prescribe q(t), calcula v=JL qdot y contrasta con diferencias centrales. Los tests también comprueban derivación simbólica, orientación, rangos y entradas inválidas.

La validación actual es matemática y numérica. No incluye flexibilidad, contacto, hardware ni medidas reales. Las decisiones de integración se registran en las notas internas.
