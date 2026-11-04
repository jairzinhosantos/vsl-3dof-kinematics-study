# Reproduce · mantenimiento opcional

El [informe PDF](../report/output/report.pdf) y las [gráficas](../simulations/README.md) se entregan listos. Estos comandos sólo son necesarios para repetir cálculos o modificar la entrega.

Se ejecutan desde la raíz del repositorio. Se requiere Python 3.11 o superior y [uv](https://docs.astral.sh/uv/).

## Preparar y comprobar

```sh
uv sync --locked
uv run python run.py test
```

## Repetir los métodos del curso

```sh
uv run python run.py course --run-id run-002
```

Genera directa, inversa, espacio de trabajo, interpoladores y control en `simulations/course/results/run-002/`. Allí quedan CSV, gráficas, métricas y procedencia.

`run-001` contiene la evidencia utilizada por el informe actual. Cada ejecución nueva requiere otro identificador; si `run-002` existe, se utiliza `run-003`. Para llevar resultados nuevos al informe se actualizan sus cifras y rutas de figuras antes de compilar.

## Repetir la trayectoria diferencial

```sh
uv run python run.py simulate --run-id run-002
```

Salida: `simulations/differential/results/run-002/`.

| Archivo | Contenido |
|---|---|
| `diagnostics.png` | Posición, velocidad, error numérico y condicionamiento |
| `robot-motion.html` | Visor 3D para descargar y abrir en un navegador |
| `trajectory.csv` | Valores calculados por instante |
| `motion.json` | Poses utilizadas por Blender |
| `manifest.json` | Configuración, procedencia y comprobaciones |

Blender es opcional, se instala por separado y utiliza esa misma ejecución:

```sh
uv run python run.py blender --run-id run-002
```

La escena y su vista previa quedan en la subcarpeta `blender/` de esa ejecución. El cálculo no requiere Blender.

El caso de ruido sintético también es opcional:

```sh
uv run python run.py dummy --run-id run-002
```

Salida: `simulations/dummy-sensor/results/run-002/`.

## Actualizar el PDF

Requiere TeX Live o MacTeX con `latexmk`, `pdflatex` y `biber`:

```sh
uv run python run.py report
uv run python run.py test
```

Se suben las fuentes modificadas, `report/output/report.pdf` y `report/output/build.json` en el mismo PR. Los archivos auxiliares de compilación permanecen ignorados. El CI comprueba el PDF preparado sin necesitar LaTeX.

Ayuda de comandos: `uv run python run.py --help`.

## Estudiar con notebooks

La [guía de estudio](../notebooks/README.md) permite leer las salidas en GitHub. Para abrirlos localmente: `uv run --group study jupyter lab notebooks`. Para comprobarlos desde cero: `uv run --group study python run.py notebooks`. El grupo `study` contiene Jupyter y se instala con `uv sync --locked --group study`.
