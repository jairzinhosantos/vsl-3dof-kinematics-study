# VSL 3-DOF Kinematics · MIA UNI Midterm

Replicación del paper de Ramzy et al. (2024) para el trabajo parcial de Robótica y Sistemas Autónomos de la **Maestría en Inteligencia Artificial de la Universidad Nacional de Ingeniería**.

El trabajo desarrollará la cinemática directa, inversa y diferencial, el análisis de singularidades y el control cinemático de un robot antropomórfico de tres grados de libertad. Incluye un informe LaTeX, código Python, pruebas y simulaciones.

[Paper seleccionado](docs/paper.md) · [Modelo del robot](docs/model.md) · [Informe](report/main.tex) · [Tablero](https://github.com/users/jairzinhosantos/projects/4)

## Organización

| Carpeta | Contenido |
|---|---|
| `docs/` | Requisitos, explicación del paper y desarrollo matemático |
| `report/` | Documento LaTeX y PDF generado en `report/output/report.pdf` |
| `code/` | Cálculo del robot, simulación, visualización y pruebas |
| `simulations/` | Configuración y resultados de cada caso |
| `assets/` | Logo UNI y figuras del documento |

`run.py` es el único punto de entrada para ejecutar el proyecto. Los módulos de `code/` son utilizados por ese archivo; no se ejecutan uno por uno.

## Orden de revisión

1. [Requisitos del parcial](docs/assignment.md).
2. [Resumen del paper](docs/paper.md) y [modelo matemático](docs/model.md).
3. [Cinemática diferencial](docs/differential.md).
4. [Simulación de movimiento](simulations/differential/README.md).
5. [Informe LaTeX](report/main.tex).

Existe **un solo robot**. La simulación diferencial calcula su movimiento; el visor HTML y Blender representan esa misma trayectoria. El caso `dummy-sensor` sólo genera observaciones sintéticas con ruido para probar el procesamiento de datos: es opcional y no representa otro robot ni mediciones del artículo.

## Orden de ejecución

Los comandos se ejecutan desde la raíz del repositorio. Se requiere Python 3.11 o superior y [uv](https://docs.astral.sh/uv/).

**1. Preparar el entorno** — una vez después de descargar el repositorio:

```sh
uv sync --locked
```

**2. Comprobar el modelo y los archivos:**

```sh
uv run python run.py test
```

**3. Ejecutar la simulación principal:**

```sh
uv run python run.py simulate --run-id run-002
```

Los resultados quedan juntos en `simulations/differential/results/run-002/`:

| Archivo | Qué muestra |
|---|---|
| `diagnostics.png` | Posición, velocidad, error numérico y condicionamiento |
| `robot-motion.html` | Movimiento 3D interactivo; se abre en un navegador |
| `trajectory.csv` | Valores calculados en cada instante |
| `motion.json` | Poses utilizadas por Blender |
| `manifest.json` | Configuración, procedencia y comprobaciones |

`run-001` contiene los resultados iniciales. Cada ejecución nueva requiere un identificador distinto; si `run-002` ya existe, se utiliza `run-003`.

**4. Generar la vista Blender — opcional, después del paso 3:**

```sh
uv run python run.py blender --run-id run-002
```

Requiere Blender instalado. La escena `.blend` y la vista previa se guardan en `simulations/differential/results/run-002/blender/`. No se necesita Blender para ejecutar el cálculo ni para abrir el visor HTML.

**5. Exportar el informe:**

```sh
uv run python run.py report
```

Requiere TeX Live o MacTeX con `latexmk`, `pdflatex` y `biber`. El PDF queda en `report/output/report.pdf`, separado de las simulaciones.

La prueba de datos dummy se ejecuta por separado, cuando se necesite:

```sh
uv run python run.py dummy --run-id run-002
```

Sus resultados quedan en `simulations/dummy-sensor/results/run-002/`. La ayuda general está disponible con `uv run python run.py --help`.
