# Working agreements

- Este es un parcial sobre un paper ya elegido. Mantener una estructura simple: notas, informe, código, pruebas, simulaciones y assets. No añadir capas de gestión, carpetas vacías ni herramientas sin una necesidad concreta.
- Carpetas, archivos y código en inglés; explicaciones en español. Leer README.md y docs/assignment.md antes de cambiar alcance.
- Python es el entorno principal. El modelo rígido es provisional. Distinguir parámetros publicados, supuestos, datos sintéticos y mediciones reales; una animación no valida comportamiento físico.
- El informe organiza desarrollo y conclusiones por tema, sin nombres de integrantes en las secciones. Los desarrollos propuestos se revisan en PR; docs/differential.md conserva la nota de estudio. Entregar el PDF preparado junto con sus fuentes y actualizar report/output/build.json al compilar.
- Conservar la consigna y el paper originales en _local, el material de clase en assets/utility y el logo suministrado por el equipo en assets/logos. No inventar el logo ni opiniones personales. No sobrescribir resultados históricos.
- El tablero GitHub es la única lista de tareas y tiene tres estados: Backlog, In Progress y Review. No mantener un plan paralelo en JSON ni sincronizadores de estados.
- Las ramas de trabajo abren PR hacia develop. Sólo Jairzinho decide integrar. Un merge no implica aceptación académica de todo el contenido.
- El agente llega como máximo a Review. Solo Jairzinho revisa y decide integrar los PRs, cierra issues como completadas, mueve tarjetas a Done si vuelve a usar ese estado y asigna Completed date. No fusionar PRs ni habilitar auto-merge.
- No configurar automatizaciones que lleven tarjetas a Done o cierren issues por eventos de PRs o checks. Un CI correcto o un merge previo no equivale a aceptación del usuario. Usar Refs #N, sin palabras de cierre automático.
- Ejecutar uv run python run.py test. Si se cambian rutas de simulación o LaTeX, comprobar también esa ejecución. Comprobar visualmente figuras modificadas.
- No enviar mensajes a personas ni delegar en subagentes sin autorización explícita aplicable.

- README e informe en tercera persona y redacción impersonal, breve y directa. Acuerdos, responsables y consultas al profesor sólo en docs/internal.md. PRs y tareas con descripciones breves.
- run.py es la entrada de ejecución. Código en code/, PDF en report/output/ y visualizaciones junto a su simulación; no crear una carpeta global outputs.
