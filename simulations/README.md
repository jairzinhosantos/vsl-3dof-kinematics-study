# Simulations

- [Differential](differential/README.md): trayectoria prescrita y contraste de velocidades.
- [Dummy sensor](dummy-sensor/README.md): datos sintéticos para probar el flujo de datos; apoyo opcional, no parte experimental del paper.

Cada caso guarda su configuración y resultados. Para ejecutar ambos:

```sh
uv run python scripts/run_experiments.py --run-id run-002
```

Usar otro identificador si ya existe. El visor queda en `outputs/<run-id>/robot-motion.html`. [Uso de Blender](../docs/simulation.md).

## Resultados conservados

`run-001` conserva exactamente los archivos y hashes de la ejecución inicial, aprobada por las comprobaciones numéricas y pendiente de revisión humana. Se movieron de `experiments/exp-001-differential/` a `simulations/differential/` y de `experiments/exp-002-dummy-sensor/` a `simulations/dummy-sensor/`. Las rutas y hashes de código dentro de esos manifiestos son históricos: corresponden al commit `55b3772`. Los nuevos manifiestos usan las rutas actuales.

17 pruebas pasaron en la versión inicial. Blender 5.1.2 produjo una escena de 201 poses y un render. No se han ejecutado dinámica flexible, contacto, controlador ni ensayos físicos. Las versiones Python están fijadas en `uv.lock`.

Los CSV y SVG conservan sus bytes originales; `.gitattributes` evita normalizar las evidencias. El historial Git y `_local/history/before-simplification/` conservan la organización anterior. Se retiraron documentación administrativa redundante, sincronización del tablero, adaptación MATLAB y carpeta anticipada de presentaciones; el código y las evidencias útiles siguen activos.

## Comprobación tras simplificar

Se repitieron las 17 pruebas y la simulación con las rutas actuales (`structure-check`): error de velocidad dentro de tolerancia y RMSE dummy de 0.00350455 m. Los resultados temporales se conservaron en `_local/structure-check/` para no duplicar evidencia en Git. Blender cargó la nueva ruta y guardó la escena correctamente. El informe compiló a PDF de seis páginas y se revisó visualmente; sigue siendo una plantilla pendiente de completar.
