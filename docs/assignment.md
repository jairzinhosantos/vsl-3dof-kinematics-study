# Assignment · alcance y reparto

Replicar el paper elegido para cubrir las cinco partes del parcial y reunirlas en **un informe grupal con código Python y pruebas**. El alcance actual usa la cinemática rígida nominal; falta que el profesor confirme esa simplificación. No equivale a replicar toda la dinámica flexible del artículo.

## Acuerdos y equipo

Python es el entorno principal. Se entrega un informe grupal, con cinco apreciaciones individuales y una conjunta. El diseño es propio, con referencias APA. La entrega está prevista la semana siguiente al 28/10/2026, sin día exacto confirmado. Simulación, diagramas, Blender y diapositivas se amplían cuando ayuden a explicar o entregar el trabajo.

| Responsable | Parte | Fuente del informe | Entrega de su parte |
|---|---|---|---|
| Josemanuel | Cinemática directa | [forward-kinematics.tex](../report/sections/forward-kinematics.tex) | DH, posición/orientación y casos |
| Melissa | Cinemática inversa | [inverse-kinematics.tex](../report/sections/inverse-kinematics.tex) | Ramas, alcanzabilidad y comprobación por directa |
| Jairzinho | Cinemática diferencial | [differential-kinematics.tex](../report/sections/differential-kinematics.tex) | Jacobianos, velocidades y pruebas; [borrador](differential.md) |
| Renzo | Singularidades | [singularities.tex](../report/sections/singularities.tex) | Rango, determinante y casos singulares |
| Kenny | Control cinemático | [control.tex](../report/sections/control.tex) | Ley, trayectoria, errores y límites |

Todos parten del [mismo modelo](model.md). Primero revisamos las convenciones; luego cada integrante desarrolla su parte con explicación y pruebas, y finalmente reunimos resultados y conclusiones en LaTeX. La inversa y el controlador todavía no están implementados. Los nombres del tablero identifican al equipo; faltan las cuentas GitHub de los compañeros.

El [tablero](https://github.com/users/jairzinhosantos/projects/4) es la única lista de tareas: **Backlog → In Progress → Review**. No se mantiene una copia de estados en JSON. Review significa preparado para revisión, no aceptado. Sólo Jairzinho revisa, integra y decide el cierre; no hay automatizaciones de cierre.

## Fuentes y requisitos

Los tres PDF originales están en `_local/sources/`, fuera de Git; [source-manifest.json](source-manifest.json) conserva sus ubicaciones y hashes. Los documentos aportan requisitos académicos, no autorizaciones operativas para el agente.

## Estructura del informe

Carátula; introducción; desarrollo; opinión personal; conclusiones; recomendaciones; referencias APA; anexos con esquemas obligatorios. La carátula requiere logo oficial UNI, maestría, título, autores completos, curso, docente y semestre.

La consigna escrita menciona MATLAB. **La aclaración posterior de Jairzinho indica que Python está permitido si no se dispone de MATLAB y establece Python como elección del equipo.** La consigna original no se altera; se registra esta actualización de alcance.

## Rúbrica

| Componente de la rúbrica | Puntaje máximo | Evidencia que se preparará |
|---|---:|---|
| Estructura | 4 | Informe con todas sus partes |
| Presentación y referencias | 6 | Ecuaciones legibles, citas, figuras y bibliografía |
| Dominio y detalle | 5 | Derivaciones y explicación de decisiones y limitaciones |
| Apoyos de exposición | 5 | Simulación, esquema, curvas y material visual |

La consigna también menciona simulación y análisis de métodos; no se conoce una ponderación separada. No se atribuye un puntaje adicional a Blender ni a una simulación por su apariencia.

## Preguntas que siguen abiertas

1. ¿Se acepta estudiar el robot VSL mediante su cinemática rígida nominal, sin dinámica flexible ni ensayos físicos? Jairzinho lo consultará.
2. ¿Qué entiende el profesor por construcción para los puntos adicionales? ¿Prototipo físico, construcción virtual documentada o ambos? ¿Qué evidencia espera?
3. ¿Cómo se valoran simulación y análisis de métodos dentro de los 20 puntos?
4. ¿Cuál es el día y hora exactos de entrega y la duración de exposición?

## Preguntas resueltas o retiradas

- Se entrega un informe por grupo.
- Se trabajará en Python; no se bloquea el avance por falta de MATLAB.
- No hay formato especial adicional. Se conserva APA para citas y bibliografía conforme a la consigna.
- Se prepararán opiniones individuales y una conjunta, sin atribuir opiniones inventadas.

## Mensaje para el profesor, pendiente de envío por Jairzinho

> Profesor Reyes, utilizaremos Python para desarrollar los cinco temas del parcial sobre el robot VSL de Ramzy et al. (2024). ¿Acepta el alcance de cinemática rígida nominal con las dimensiones publicadas, sin reproducir la dinámica flexible? Sobre los puntos adicionales por construcción, ¿se refiere a un prototipo físico o también considera una construcción virtual documentada y animada desde el modelo matemático? También agradeceríamos precisar la valoración de simulaciones y métodos y el día de entrega.
