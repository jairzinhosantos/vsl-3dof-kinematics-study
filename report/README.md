# Group report

[main.tex](main.tex) reúne las secciones del informe. Cada integrante trabaja en el archivo de su tema dentro de `sections/`; el [reparto](../docs/assignment.md) enlaza las cinco partes. `preamble.tex` y `references.bib` se mantienen aquí, sin copias compartidas.

El [borrador diferencial](../docs/differential.md) sigue separado hasta su revisión. Hay cinco apreciaciones individuales y una conjunta. Colocar el logo oficial en `assets/branding/uni-logo.png` o `.pdf`; faltan nombres completos y datos de carátula.

Exportar cuando haga falta:

```sh
uv run python scripts/build_report.py
```

Requiere latexmk, pdflatex y biber (TeX Live/MacTeX). Salida: `outputs/report/group-report.pdf`. Los PDF antiguos son historial local, no una entrega actualizada.
