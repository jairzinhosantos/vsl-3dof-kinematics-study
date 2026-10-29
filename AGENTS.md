# Working agreements

- Carpetas, archivos, funciones y claves de configuración en inglés; contenido explicativo en español. Conservar títulos bibliográficos originales.
- Leer README.md, docs/project-charter.md y la tarea antes de cambiar alcance. Python es el entorno principal, aceptado según aclaración de Jairzinho; MATLAB es un adaptador opcional.
- Markdown es la base de estudio. Generar PDF, diapositivas y renders cuando aporten evidencia o sirvan para revisión/entrega. No mantener versiones contradictorias del mismo texto.
- Distinguir parámetros publicados, hipótesis, datos sintéticos, mediciones reales y resultados reproducidos. La animación no prueba comportamiento físico ni aceptación académica.
- Cada experimento incluye protocolo, entradas, semilla si aplica, criterio, límite de ejecución y evidencia. No sobrescribir ejecuciones históricas aprobadas o presentadas.
- Conservar las fuentes institucionales y archivos locales en _local, fuera de Git. assets/branding recibe el logo proporcionado por el equipo; no inventarlo.
- main y develop contienen únicamente el bootstrap hasta la primera revisión. Las tareas se preparan en ramas cortas y PRs hacia develop. El bootstrap administrativo no implica aceptación de contenido académico.
- El agente llega como máximo a Review. Solo Jairzinho revisa y decide integrar los PRs, cierra issues como completadas, mueve tarjetas a Done y asigna Completed date. No fusionar PRs ni habilitar auto-merge.
- No configurar automatizaciones que lleven tarjetas a Done o cierren issues por eventos de PRs o checks. Un CI correcto o un merge previo no equivale a aceptación del usuario. Usar Refs #N en los PRs, sin palabras de cierre automático.
- Ejecutar uv run pytest y uv run python scripts/check_repository.py; comprobar visualmente figuras modificadas. No ejecutar servicios o consumir recursos externos en CI.
- No programar automatizaciones, enviar mensajes a personas ni delegar en subagentes sin autorización explícita aplicable.
