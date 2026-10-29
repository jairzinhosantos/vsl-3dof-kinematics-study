# Report

[main.tex](main.tex) reúne introducción, resumen del paper, desarrollo, resultados, conclusiones por tema y general, recomendaciones, referencias y anexos. Los temas tienen archivos separados dentro de `sections/`; no llevan nombres de integrantes.

El PDF se genera desde la raíz del repositorio:

```sh
uv run python run.py report
```

Salida: `report/output/report.pdf`. Requiere TeX Live/MacTeX con `latexmk`, `pdflatex` y `biber`. La portada utiliza [uni-logo.png](../assets/logos/uni-logo.png).

El [borrador diferencial](../docs/differential.md) continúa separado hasta revisión. La plantilla distingue los apartados aún pendientes de los resultados disponibles.
