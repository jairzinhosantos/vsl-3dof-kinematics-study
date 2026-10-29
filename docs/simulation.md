# Simulation · un modelo, distintas salidas

El proyecto utiliza un robot RRR con dimensiones tomadas del paper. [model.py](../code/model.py) calcula posiciones y Jacobianos; [motion.py](../code/motion.py) define una trayectoria articular y evalúa sus velocidades.

| Salida | Función | Cálculo independiente |
|---|---|---|
| Curvas y CSV | Cuantificar posición, velocidad y error | Modelo Python |
| Visor HTML | Examinar el movimiento en 3D | Usa las posiciones calculadas |
| Blender | Producir una escena y render del mismo movimiento | Lee `motion.json` |
| Datos dummy | Probar el flujo de datos con ruido diseñado | Caso opcional del mismo robot |

El orden es **pruebas → simulación → visualización → informe**. Los [comandos del README](../README.md#orden-de-ejecución) ejecutan cada paso. Blender requiere primero una simulación existente con el mismo `run-id`.

La implementación actual evalúa movimiento prescrito de eslabones rígidos. El control de seguimiento aún no está implementado. La visualización no incluye flexibilidad, contacto ni ensayos físicos; los datos dummy tampoco constituyen mediciones reales.

NumPy realiza los cálculos, SymPy comprueba expresiones, Matplotlib produce las curvas y Plotly el visor. Blender sólo es necesario para generar la escena `.blend`. Las dependencias Python están fijadas en `uv.lock`.
