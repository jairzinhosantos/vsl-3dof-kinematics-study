# Simulation stack

## Capas elegidas

| Capa | Herramienta | Uso actual |
|---|---|---|
| Cálculo | NumPy | Transformaciones, Jacobianos y trayectoria |
| Derivación | SymPy | Comprobación simbólica del determinante |
| Verificación | pytest | Contrastes independientes y casos límite |
| Figuras | Matplotlib | Curvas de posición, velocidad, error y condicionamiento |
| Exploración | Plotly | Visor 3D offline con reproducción y deslizador temporal |
| Construcción virtual | Blender | Escena esquemática animada desde posiciones exportadas |
| Documento | Markdown y LaTeX | Estudio continuo y exportación del informe cuando proceda |

Python y Blender son herramientas de código abierto. El código no depende de MATLAB. La escena utiliza eslabones rígidos geométricos y una trayectoria prescrita; no implementa contacto, actuadores ni flexibilidad.

## Blender

Se detectó Blender 5.1.2 ya instalado. La [documentación oficial](https://docs.blender.org/manual/en/latest/advanced/command_line/render.html) admite ejecución y render en segundo plano. El script del proyecto carga `motion.json`, verifica metros, crea base, eslabones y articulaciones, inserta poses y guarda `.blend`. Las posiciones vienen del modelo probado; la geometría es una representación propia simplificada.

La animación contiene 201 poses a 20 fps. Las longitudes visuales son las del modelo. Blender interpola entre keyframes; esa interpolación visual no se utiliza para calcular métricas científicas. El JSON y el CSV conservan los datos calculados por Python.

## ¿Hace falta un motor físico?

Para la cinemática y control de posición nominal, el cálculo directo y la integración cinemática pueden realizarse en Python. Si el docente exige contacto, actuadores o dinámica, evaluar [MuJoCo y su API Python](https://mujoco.readthedocs.io/en/stable/python.html). No se instaló un motor físico ni se añadieron masas o rigideces arbitrarias. Esa ampliación depende del alcance y de parámetros verificables.

Las [herramientas de animación de Matplotlib](https://matplotlib.org/stable/api/animation_api.html) son otra opción para generar GIF/video sin Blender. Se prioriza primero un modelo validado numéricamente y una visualización comprensible.

## Reproducir las vistas

`uv run python scripts/run_experiments.py --run-id run-002` crea curvas y un HTML autónomo. Abrir `outputs/run-002/robot-motion.html` en un navegador. No necesita red para mostrar la animación.

`blender --background --factory-startup --python-exit-code 1 --python scripts/build_blender_scene.py -- --render-preview` crea escena y vista previa. El script acepta `--motion <ruta>` y `--output <carpeta>`.

Los permisos del proceso o del dispositivo gráfico pueden afectar Blender en entornos aislados. Registrar fallos de ejecución y conservar siempre la simulación numérica como evidencia independiente de la visualización.
