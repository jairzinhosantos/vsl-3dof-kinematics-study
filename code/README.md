# Code

El código respalda el [informe preparado](../report/output/report.pdf) y los [resultados](../simulations/README.md). La reproducción es opcional y se realiza desde `run.py`, sin instalar el proyecto como paquete.

| Archivo | Función |
|---|---|
| `model.py` | DH, geometría del robot y Jacobianos |
| `course.py` | Directa geométrica y MTH, inversa, interpoladores y control |
| `course_demo.py` | Casos de clase y exportación de sus resultados |
| `motion.py` | Trayectoria articular y velocidades |
| `simulate.py` | Datos, curvas y visor HTML del caso diferencial |
| `blender_scene.py` | Escena Blender a partir de `motion.json` |
| `tests/` | Comprobaciones matemáticas y numéricas |
| `check_project.py` | Enlaces, integridad de resultados y correspondencia del PDF |

La compilación del documento pertenece a `report/build.py`. [Comandos opcionales](../docs/reproduce.md).
