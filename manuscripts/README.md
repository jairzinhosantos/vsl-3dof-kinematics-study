# Manuscripts

`report/main.tex` es la plantilla grupal. Las notas activas están en `research/` y `docs/`. El borrador diferencial no se importa automáticamente: Jairzinho revisa antes de integrarlo.

Se conservaron las ocho partes de la consigna y se actualizó el entorno a Python. Hay cinco apreciaciones individuales y una conjunta. El logo se lee de `assets/branding`.

Exportar cuando sea necesario: `python3 scripts/build_report.py`. Requiere latexmk, pdflatex y biber. La salida queda en `outputs/report/`. El script sincroniza preámbulo y referencias desde `common/`. No genera PDF en cada edición de Markdown.

Los PDF anteriores permanecen sólo como historial local y no representan los acuerdos vigentes. La vista previa automática de la app puede no localizar Biber; la compilación local cuenta con el ajuste de arquitectura para MacTeX ya comprobado en la primera versión.
