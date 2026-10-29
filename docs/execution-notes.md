# Execution notes

## Ejecución inicial v0.2

- Python 3.12.14; NumPy 2.5.4; Matplotlib 3.11.2; SymPy 1.14.0; Plotly 6.9.0. Las dependencias completas están en uv.lock.
- 17 pruebas aprobadas, incluyendo verificación simbólica del determinante.
- Exp-001 y exp-002 ejecutados como run-001; manifiestos y archivos conservados junto al protocolo.
- Blender 5.1.2: escena de 201 poses, render de vista previa y manifiesto generados. La ejecución inicial dentro del sandbox terminó antes de ejecutar el script; la ejecución autorizada fuera de ese aislamiento finalizó correctamente.
- El primer lanzamiento de experimentos detectó que el paquete editable se había instalado antes de existir sus archivos. Se reinstaló el paquete local y se ejecutaron los protocolos. Ese intento no produjo un conjunto de resultados.
- GitHub CLI funciona con acceso de red. El conector no accedía al repositorio privado recién creado; la configuración se realizó con CLI y la UI para desactivar automatizaciones.

La escena animada comprueba visualización cinemática. No se ha ejecutado dinámica flexible, simulación de contacto, controlador de seguimiento ni ensayo físico. Los fallos de entorno no se presentan como fallos del modelo.
- Los CSV y SVG generados conservan exactamente sus bytes para que los hashes sigan siendo verificables. `.gitattributes` evita normalización de finales de línea y omite reglas de espacios sólo en resultados generados.
