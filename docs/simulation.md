# Simulation · un modelo, distintos casos

El proyecto utiliza un robot RRR con dimensiones tomadas del paper. Los [resultados preparados](../simulations/README.md) se pueden revisar sin ejecutar código.

| Caso o representación | Función |
|---|---|
| `course` | Comparar métodos de directa, resolver inversa, interpolar y controlar posición/seguimiento |
| `differential` | Prescribir una trayectoria articular y comprobar velocidades |
| Visor HTML y Blender | Representar la misma trayectoria diferencial calculada |
| `dummy-sensor` | Probar el procesamiento con ruido sintético |

El control utiliza la pseudoinversa del Jacobiano de posición y Euler explícito, siguiendo la semana 9. Se comprueban la reducción del error y el efecto del paso temporal; un caso singular muestra estancamiento. No se incluyen saturación, flexibilidad, contacto ni ensayos físicos.

Para modificar resultados, el orden es **cálculo → gráficas → informe → comprobaciones**. La [guía opcional](reproduce.md) reúne los comandos. Blender requiere una ejecución diferencial previa con el mismo identificador.

NumPy realiza los cálculos, SymPy comprueba expresiones, Matplotlib produce curvas y Plotly el visor. Blender sólo se necesita para generar la escena `.blend`. Las dependencias Python están fijadas en `uv.lock`.
