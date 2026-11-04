# VSL 3-DOF Kinematics · MIA UNI Midterm

Replicación del paper de Ramzy et al. (2024) para el trabajo parcial de Robótica y Sistemas Autónomos de la **Maestría en Inteligencia Artificial de la Universidad Nacional de Ingeniería**.

El trabajo desarrolla la cinemática directa, inversa y diferencial, las singularidades y el control cinemático de un robot antropomórfico de tres grados de libertad. Los métodos siguen los materiales del curso y se comprueban mediante simulaciones en Python.

**[Consultar informe PDF](report/output/report.pdf)** · [Fuentes LaTeX](report/main.tex) · [Resultados y gráficas](simulations/course/README.md) · [Tablero](https://github.com/users/jairzinhosantos/projects/4)

El informe y los resultados se incluyen listos para consultar. No se requiere instalar herramientas ni ejecutar código para revisarlos. La versión actual es el **borrador 04**, preparado para revisión.

## Orden de lectura

1. [Informe PDF](report/output/report.pdf): introducción, resumen del paper, desarrollo, resultados y conclusiones.
2. [Correspondencia con las clases](docs/course-alignment.md): métodos, notación y adaptaciones al robot elegido.
3. [Resultados de simulación](simulations/course/README.md): directa, inversa, interpolación y control.
4. [Código y pruebas](code/README.md): implementación que respalda los resultados.

Como referencia: [requisitos del parcial](docs/assignment.md), [paper seleccionado](docs/paper.md), [modelo](docs/model.md) y [cinemática diferencial](docs/differential.md).

## Organización

| Carpeta | Contenido |
|---|---|
| `docs/` | Requisitos y explicación del desarrollo |
| `report/` | Informe LaTeX y PDF listo en `output/` |
| `code/` | Cálculos, generación de resultados y pruebas |
| `simulations/` | Configuración, datos y gráficas de cada caso |
| `assets/` | Logo UNI, figuras y material de clases en `utility/` |

Existe **un solo modelo de robot**. El caso `course` reúne las comprobaciones de los métodos de clase. El caso `differential` examina una trayectoria articular y contiene su visor 3D y escena Blender. `dummy-sensor` es una prueba opcional de datos con ruido. Son distintos experimentos sobre el mismo robot; sus datos son sintéticos.

## Reproducción opcional

[La guía de reproducción](docs/reproduce.md) explica cómo instalar el entorno, repetir las simulaciones y recompilar el informe. `run.py` reúne los comandos; los módulos de `code/` no se ejecutan uno por uno.
