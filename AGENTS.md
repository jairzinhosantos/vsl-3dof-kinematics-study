# Working agreements

- Este es un parcial sobre un paper ya elegido. Mantener una estructura simple: notas, informe, código, pruebas, simulaciones y assets. No añadir capas de gestión, carpetas vacías ni herramientas sin una necesidad concreta.
- Carpetas, archivos y código en inglés; explicaciones en español. Leer README.md y docs/assignment.md antes de cambiar alcance.
- Python es el entorno principal. El modelo rígido es provisional. Distinguir parámetros publicados, supuestos, datos sintéticos y mediciones reales; una animación no valida comportamiento físico.
- Cada integrante desarrolla su parte del informe y las pruebas necesarias. El borrador diferencial permanece en docs/differential.md hasta revisión. Generar PDF, diapositivas o renders cuando sean útiles.
- Conservar las fuentes originales en _local y el logo suministrado por el equipo en assets/branding. No inventar el logo ni opiniones personales. No sobrescribir resultados históricos.
- El tablero GitHub es la única lista de tareas y tiene tres estados: Backlog, In Progress y Review. No mantener un plan paralelo en JSON ni sincronizadores de estados.
- Las ramas de trabajo abren PR hacia develop. Sólo Jairzinho decide integrar. El bootstrap de main/develop no implica aceptación académica.
- El agente llega como máximo a Review. Solo Jairzinho revisa y decide integrar los PRs, cierra issues como completadas, mueve tarjetas a Done si vuelve a usar ese estado y asigna Completed date. No fusionar PRs ni habilitar auto-merge.
- No configurar automatizaciones que lleven tarjetas a Done o cierren issues por eventos de PRs o checks. Un CI correcto o un merge previo no equivale a aceptación del usuario. Usar Refs #N, sin palabras de cierre automático.
- Ejecutar uv run pytest y uv run python scripts/check_repository.py. Si se cambian rutas de simulación o LaTeX, comprobar también esa ejecución. Comprobar visualmente figuras modificadas.
- No enviar mensajes a personas ni delegar en subagentes sin autorización explícita aplicable.
