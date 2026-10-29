# Shared model · robot RRR

El modelo utiliza la geometría rígida nominal del robot descrito en el paper.

Las tres articulaciones son rotacionales. Se adopta DH estándar `Rz(q) Tz(d) Tx(a) Rx(alpha)`, base fija, radianes, metros y vectores columna. Con q=0 los eslabones están alineados sobre +x a altura l1.

| i | theta | alpha | a | d |
|---:|---|---|---|---|
| 1 | q1 | pi/2 | 0 | l1 |
| 2 | q2 | 0 | l2 | 0 |
| 3 | q3 | 0 | l3 | 0 |

Longitudes: l1=0.04 m, l2=0.29 m, l3=0.24 m; [paper](paper.md), tabla 2.

Definiendo una coordenada radial con signo y una altura relativa:

$$\rho=l_2\cos q_2+l_3\cos(q_2+q_3),\qquad h=l_2\sin q_2+l_3\sin(q_2+q_3),$$

$$p(q)=[\cos q_1\rho,\;\sin q_1\rho,\;l_1+h]^T.$$

No confundir rho con la distancia no negativa sqrt(x²+y²). Las transformaciones se reconstruyen desde DH para evitar copiar las erratas del artículo.

## Contrato del código

- `dh(theta,d,a,alpha)` conserva el orden de argumentos de clase; todos los ángulos están en radianes.
- `forward(q)` devuelve M03, orígenes previos y ejes articulares en la base.
- `jacobian(q)` devuelve JL, Jw y J con orden `[v;omega]`.
- `joint_points(q)` devuelve base, hombro, codo y efector, en metros.
- Las funciones rechazan formas distintas de `(3,)`, valores no finitos y longitudes no positivas.

No se conocen límites físicos completos. Los rangos de pruebas son rangos matemáticos, no especificaciones de actuadores. No hay masas, torques, presión ni deformaciones en esta versión.
