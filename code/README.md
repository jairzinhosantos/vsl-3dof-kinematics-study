# Code

La ejecución se realiza con `run.py`, desde la raíz. No requiere instalar el código como paquete.

| Archivo | Función |
|---|---|
| `model.py` | Geometría del robot, transformaciones y Jacobianos |
| `motion.py` | Trayectoria articular y cálculo de velocidades |
| `simulate.py` | Exportación de datos, curvas y visor HTML |
| `blender_scene.py` | Escena Blender construida desde `motion.json` |
| `tests/test_model.py` | Comprobaciones matemáticas y numéricas |
| `check_project.py` | Enlaces y archivos de resultados |

La exportación del informe pertenece a `report/build.py`. [Orden de ejecución](../README.md#orden-de-ejecución).
