# Simulations

Ambos casos usan el mismo robot:

- [Differential](differential/README.md): caso principal; calcula movimiento, velocidades y error numérico.
- [Dummy sensor](dummy-sensor/README.md): prueba opcional de observaciones sintéticas con ruido.

Cada carpeta contiene `config.json` y `results/<run-id>/`. Las gráficas, datos, HTML y escena Blender quedan junto a la ejecución que los produjo. El PDF del informe pertenece a `report/output/`.

Los archivos `run-001` conservan sus bytes originales. Sus manifiestos describen las rutas de la primera ejecución (commit `55b3772`); los manifiestos nuevos usan la estructura actual. Las carpetas locales `preview` se reservan para comprobar cambios sin añadir resultados duplicados a Git.
