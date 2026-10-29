# ADR-001 · Python and evidence-first study

Fecha: 2026-10-28. Estado: decisión de organización aplicada; contenido técnico en Review.

## Contexto

La primera entrega organizaba carpetas numeradas y usaba LaTeX/PDF para casi toda la documentación. Jairzinho pidió una estructura de estudio similar a Thinking Harness, nombres técnicos en inglés, contenido en español, Python y GitHub Projects.

## Decisión

1. Organizar por responsabilidad: docs, research, código compartido, experimentos, tests, assets y manuscrito.
2. Usar Markdown como fuente activa de comprensión. Conservar LaTeX para el informe final.
3. Python es el motor principal conforme a la aclaración del usuario. El adaptador MATLAB queda opcional, sin bloquear la entrega.
4. Un único modelo matemático genera las posiciones que alimentan el visor y Blender.
5. Guardar datos dummy con origen, semilla y ruido; no llamarlos experimentales.
6. Mantener el flujo de GitHub hasta Review, con integración y cierre manual de Jairzinho.

## Qué se toma de Thinking Harness

Una carpeta por unidad de estudio/experimento, protocolos antes de conclusiones, evidencia identificable, decisiones explícitas, enlaces relativos y revisión humana. Se evita replicar sus reglas de idioma inglés integral, su amplitud de tesis y su infraestructura futura.

## Migración y conservación

Los archivos originales se verificaron por SHA-256. La estructura anterior quedó en `_local/initial-v0.1.zip` y `_local/history/`, ignorados por Git, porque no había historial Git previo que conservara esa primera revisión. Los PDF v0.1 son históricos y contienen acuerdos sustituidos: no son la versión vigente del alcance. Los resultados Python previos mantienen sus bytes originales. El documento activo de requisitos es `docs/academic/requirements.md`.

## Consecuencias

El equipo puede leer, comentar y revisar sin recompilar PDF. La aceptación de la aproximación rígida y los puntos por construcción siguen abiertos. La simulación virtual por sí sola no resuelve esas consultas.
