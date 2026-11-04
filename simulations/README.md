# Simulations

Los tres casos utilizan el mismo robot RRR y datos sintéticos:

| Caso | Propósito | Resultados listos |
|---|---|---|
| [Course](course/README.md) | Métodos de clase: directa, inversa, espacio de trabajo, interpolación y control | CSV, métricas y cuatro gráficas |
| [Differential](differential/README.md) | Velocidades sobre una trayectoria articular prescrita | Curvas, CSV, visor HTML y vista Blender |
| [Dummy sensor](dummy-sensor/README.md) | Prueba opcional de procesamiento con ruido | Observaciones sintéticas y comparación |

Cada carpeta contiene `config.json` y `results/<run-id>/`. El informe se consulta en [PDF](../report/output/report.pdf); no requiere volver a ejecutar estos casos.

Los resultados históricos de `differential` y `dummy-sensor` conservan sus bytes originales; sus manifiestos describen las rutas de su primera ejecución (commit `55b3772`). Las nuevas ejecuciones usan la estructura actual. [Reproducción opcional](../docs/reproduce.md).

La [guía de notebooks](../notebooks/README.md) explica estos casos con código visible, fundamentos y diagramas.
