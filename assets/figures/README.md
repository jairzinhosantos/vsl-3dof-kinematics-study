# Figures and provenance

`robot-preview.png` es una vista propia de Blender 5.1.2 generada con `code/blender_scene.py` a partir de `simulations/differential/results/run-001/motion.json`. El [manifiesto](blender-manifest.json) registra hashes de entrada y script.

![Robot nominal](robot-preview.png)

La representación usa cilindros y articulaciones esquemáticas con longitudes del paper. No es una fotografía, plano del fabricante, réplica CAD fiel ni validación física. El archivo `.blend` animado está en `simulations/differential/results/run-001/blender/` y es regenerable.

El manifiesto conserva la ruta y el hash históricos del script en el commit `55b3772`; sólo cambió la ubicación de las entradas en la simplificación.
