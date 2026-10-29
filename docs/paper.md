# Ramzy et al. (2024) · Paper study

Ramzy, M. R., Hammad, S., & Maged, S. A. (2024). Kinematic and Dynamic Modeling of 3DOF Variable Stiffness Links Manipulator with Experimental Validation. *Applied Sciences, 14*(12), 5285. https://doi.org/10.3390/app14125285

## Pregunta de lectura

¿Qué elementos del artículo sustentan un estudio cinemático de un robot antropomórfico real de 3 GDL, y cuáles requieren corrección, interpretación o desarrollo adicional?

## Aporte y alcance

Los autores estudian un manipulador con eslabones de rigidez variable, modelan cinemática y dinámica mediante parámetros concentrados y presentan validación experimental. El parcial utilizará provisionalmente la geometría y la cinemática rígida nominal. Esa reducción no equivale a reproducir la contribución completa del artículo.

## Evidencia útil

| Localización | Contenido | Uso en el proyecto |
|---|---|---|
| Tabla 1, p. 4 | DH estándar | Marcos y geometría |
| Ecs. (6)-(8), p. 5 | Posición del efector | Derivación diferencial |
| Tabla 2, p. 9 | l1=0.04, l2=0.29, l3=0.24 m | Parámetros nominales |
| Tabla 3, p. 14 | Posiciones teóricas y medidas por los autores | Contraste documental pendiente de reconciliación |

## Incidencias

- P-01: la ec. (2) imprime una fila nula en la rotación; DH exige `[0,1,0]`.
- P-02: la ec. (3) imprime cero en (3,3); DH exige 1.
- P-03: la ec. (5) termina en `[0,0,0,0]`; debe ser `[0,0,0,1]` para una transformación homogénea.
- P-04: los índices de la cadena se contradicen; usar T01 T12 T23.
- P-05: las ecuaciones inversas (9)-(12) requieren reconciliar altura, cuadrantes y ángulos con DH. Derivar con `z-l1` y `atan2`.
- P-06: la primera fila de la tabla 3 no coincide exactamente con las dimensiones publicadas y las ecuaciones de posición.

En P-06, q=(88.69,71.61,-86.82) grados produce y=322.9987 mm y z=252.2242 mm; la tabla publica y=324.66 mm y z=256.96 mm como valores teóricos. Las diferencias son -1.6613 y -4.7358 mm. La causa no se ha identificado; no ajustar longitudes para forzar acuerdo. La primera revisión comprobó visualmente las matrices de la p. 5; varias páginas del PDF contienen texto superpuesto.

## Claims, interpretación y evidencia propia

Los ensayos físicos pertenecen a los autores. El modelo rígido del equipo es una interpretación provisional apoyada en la sección 2.1. Las pruebas numéricas y los datos sintéticos del repositorio son evidencia propia de consistencia; no son mediciones del prototipo. No se afirma lectura exhaustiva ni reproducción de todos los resultados dinámicos.

## Siguiente lectura

Reconciliar tabla 3 y convenciones; confirmar límites articulares documentados; decidir el alcance con el profesor. La falta de datos crudos no justifica presentar datos dummy como mediciones.
