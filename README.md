# VSL 3-DOF Kinematics Study · MIA UNI Midterm

Replicación del paper de Ramzy et al. (2024) para el parcial de Robótica: cada integrante desarrolla su parte, la prueba en Python y la reunimos en un informe LaTeX. El alcance actual es la **cinemática rígida nominal**, pendiente de aceptación docente; todavía no reproduce la dinámica flexible ni los ensayos físicos del artículo.

[Tablero del equipo](https://github.com/users/jairzinhosantos/projects/4) · [Reparto y requisitos](docs/assignment.md) · [Paper elegido](docs/paper.md) · [Borrador diferencial](docs/differential.md)

## Estructura

```text
docs/          Notas del paper, requisitos, modelo y borradores
report/        Informe LaTeX: una sección por cada parte del equipo
src/           Modelo y cálculo Python compartidos
tests/         Pruebas del modelo
scripts/       Ejecutar simulaciones, exportar PDF y generar Blender
simulations/   Configuraciones, resultados y gráficas de los casos
assets/        Logo y figuras para el informe
```

`outputs/` contiene archivos regenerables, como HTML, PDF y escenas Blender. `_local/` conserva los PDF originales y respaldos. Ambas son carpetas locales excluidas de Git. Los nombres técnicos están en inglés y el contenido explicativo en español.

## Cómo trabajamos

1. Partimos del [modelo común](docs/model.md) y las dimensiones del paper.
2. Josemanuel desarrolla directa; Melissa, inversa; Jairzinho, diferencial; Renzo, singularidades; Kenny, control. Cada parte incluye explicación, código y pruebas cuando corresponda.
3. Revisamos los aportes y los reunimos en [report/main.tex](report/main.tex), con las apreciaciones individuales y una conjunta.
4. Exportamos el PDF y añadimos simulaciones o material visual útil para exponer. No se reserva una estructura para presentaciones ni un framework adicional antes de necesitarlos.

El tablero es la única lista de tareas: **Backlog → In Progress → Review**. No se duplican estados en archivos locales. Review significa listo para revisión; sólo Jairzinho decide integrar PRs y cerrar tareas. El agente no fusiona PRs ni automatiza cierres. Las propuestas van hacia `develop`; `main` y `develop` conservan el arranque administrativo mientras se revisa el primer PR.

## Ejecutar

Con Python 3.11+ y [uv](https://docs.astral.sh/uv/):

```sh
uv sync --locked
uv run pytest -q
uv run python scripts/check_repository.py
uv run python scripts/run_experiments.py --run-id run-002
```

Usar otro identificador si ya existe. Se conservan la [simulación diferencial](simulations/differential/README.md) y el [caso dummy opcional](simulations/dummy-sensor/README.md). Los datos dummy son sintéticos y no sustituyen mediciones del paper.

Abrir `outputs/<run-id>/robot-motion.html` para ver el movimiento. La [guía de simulación](docs/simulation.md) explica cómo generar la escena Blender a partir de esas mismas posiciones. No hace falta Blender para calcular ni ejecutar las pruebas.

Para exportar el informe, con TeX Live/MacTeX instalado:

```sh
uv run python scripts/build_report.py
```

La salida es `outputs/report/group-report.pdf`. El logo se coloca en [assets/branding/](assets/branding/README.md).

## Qué tenemos y qué falta

Tenemos modelo nominal, borrador diferencial, pruebas, curvas, visor 3D y escena Blender. Falta completar los aportes de los cinco, especialmente inversa y control, revisar las discrepancias del paper e integrar el informe. Las consultas sobre alcance rígido, puntuación por construcción y fecha están reunidas en [assignment.md](docs/assignment.md).

Se conserva el trabajo útil de la versión anterior; se retiraron capas administrativas, adaptación MATLAB, copias comunes de LaTeX y carpetas anticipadas. El historial permanece en Git y en `_local/history/before-simplification/`.
