# Study plan

La entrega está prevista la próxima semana respecto del 28/10/2026. No se asigna una fecha exacta sin confirmación. El tablero concentra el estado vivo; este documento define secuencia y entregas.

## Equipo y entregas

| Responsable | Bloque | Entrega revisable | Dependencias |
|---|---|---|---|
| Josemanuel | Forward kinematics | Marcos DH, posición/orientación, casos y espacio de trabajo | Acuerdo del modelo |
| Melissa | Inverse kinematics | Ramas, alcanzabilidad, límites y residuo de reconstrucción | Directa revisada |
| Jairzinho | Differential kinematics | Derivación de Jv/Jw, pruebas y curvas | Directa revisada |
| Renzo | Singularities | Rango de la tarea, determinante, SVD y casos | Jacobiano |
| Kenny | Kinematic control | Ley, ganancias, trayectoria, errores y límites | Directa y Jacobiano |
| Equipo | Integración | Introducción, opiniones individuales/conjunta, conclusiones, referencias y exposición | Evidencia de los bloques |

La correspondencia entre personas y cuentas de GitHub de los compañeros sigue pendiente. Los nombres en el tablero no implican asignaciones a usuarios desconocidos.

## Secuencia relativa a la entrega

1. **Primera sesión:** confirmar alcance rígido, construcción y fecha; revisar geometría y convenciones con Josemanuel.
2. **Desarrollo por bloques:** directa/inversa, diferencial/singularidades y diseño del control; producir evidencia local y discutir resultados.
3. **Integración técnica:** trayectoria común, casos regulares y singulares, reconstrucción inversa y seguimiento con control.
4. **Revisión del grupo:** cada integrante explica su parte y propone su apreciación; contrastar derivaciones, métricas y límites.
5. **Preparación de entrega:** integrar Markdown aprobado al informe, completar logo/autores, exportar PDF y material de exposición si se necesita.

## Brechas actuales

| Ya disponible | Falta producir o decidir |
|---|---|
| Geometría publicada y DH reconstruida | Aceptación docente de aproximación rígida |
| Modelo compartido Python y 17 pruebas | Revisión de directa por Josemanuel |
| Borrador diferencial y experimento | Aprobación del borrador por Jairzinho |
| Casos iniciales de rango | Desarrollo de singularidades de Renzo |
| Escena virtual derivada del movimiento | Confirmar si cuenta como construcción; no garantiza puntos |
| Fixture dummy con ruido diseñado | Datos físicos, si el alcance finalmente los exige |
| Plantilla de informe | Inversa, control, opiniones y conclusiones grupales |
| Repositorio, tablero y criterios | Usuarios de GitHub de los compañeros; fecha exacta |

Priorizar primero consistencia matemática y explicación. Mejorar la escena o añadir un motor físico sólo si resuelve una pregunta del trabajo y cabe en el plazo. No introducir física arbitraria para producir una animación más vistosa.
