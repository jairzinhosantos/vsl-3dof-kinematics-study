# VSL 3-DOF Kinematics Study · MIA UNI Midterm

Estudio grupal de un robot antropomórfico de tres grados de libertad, basado en Ramzy, Hammad y Maged (2024). Se desarrolla la cinemática nominal en Python y se construye una visualización 3D reproducible.

**Estado: preparación en Review.** La aceptación docente del alcance rígido está pendiente. La evidencia inicial verifica consistencia matemática; no reproduce la dinámica flexible ni ensayos físicos del artículo.

[Tablero del equipo](https://github.com/users/jairzinhosantos/projects/4) · [Plan](docs/study-plan.md) · [Acuerdos](docs/project-charter.md) · [Mapa del estudio](docs/study-map.md)

## Empezar por aquí

1. [Qué pide el parcial y qué ya se aclaró](docs/academic/requirements.md).
2. [Lectura crítica del paper](research/papers/ramzy-2024/README.md).
3. [Modelo común y convención DH](research/robot-3r/model.md).
4. [Cinemática diferencial: borrador de Jairzinho](research/robot-3r/differential.md).
5. [Experimento de velocidades](experiments/exp-001-differential/README.md) y [fixture de datos dummy](experiments/exp-002-dummy-sensor/README.md).
6. [Simulación y Blender](docs/simulation-stack.md); [qué falta y quién lo trabaja](docs/study-plan.md).

## Cómo se organiza

| Carpeta | Responsabilidad |
|---|---|
| `docs/` | Alcance, requisitos, plan, decisiones y funcionamiento del equipo |
| `research/` | Lecturas y desarrollo matemático; Markdown como base de estudio |
| `src/robotics_study/` | Modelo Python compartido entre los cinco temas |
| `experiments/` | Una carpeta por protocolo, con configuración y resultados identificados |
| `tests/` | Comprobaciones numéricas, simbólicas y de entradas |
| `scripts/` | Ejecución, gráficas, Blender, validación y exportación opcional |
| `assets/` | Logo, recursos visuales y figuras propias |
| `manuscripts/` | Plantilla LaTeX del informe grupal para la etapa de integración |
| `presentations/` | Guion de exposición; PPT sólo cuando se necesite |
| `adapters/matlab/` | Código anterior opcional; no es el motor principal |
| `_local/` | Originales institucionales e historia local, excluidos de Git |
| `outputs/` | HTML, escenas `.blend` y exportaciones regenerables, excluidos de Git |

Los nombres técnicos están en inglés y las explicaciones en español. Se adaptó la organización por evidencia de Thinking Harness; no se copió su alcance ni se creó una infraestructura de investigación innecesaria.

## Ejecutar

Se requiere Python 3.11+ y [uv](https://docs.astral.sh/uv/). Las versiones resueltas están fijadas en `uv.lock`.

```sh
uv sync --locked
uv run pytest -q
uv run python scripts/check_repository.py
uv run python scripts/run_experiments.py --run-id run-002
```

`run-001` conserva la ejecución inicial. Cada nueva ejecución usa otro identificador. El script genera resultados, manifiestos, curvas y `outputs/<run-id>/robot-motion.html`, que funciona sin conexión y permite reproducir o desplazar la animación 3D.

Para Blender, usar el ejecutable local (en macOS está dentro de `Blender.app`):

```sh
blender --background --factory-startup --python-exit-code 1 \
  --python scripts/build_blender_scene.py -- --render-preview
```

El script consume `motion.json` de `run-001` y crea una escena animada y un render en `outputs/blender/`. Puede usarse `--motion` para otra ejecución. El modelo geométrico es esquemático, no una reconstrucción CAD del prototipo físico.

## Resultados iniciales

- 17 pruebas Python aprobadas: DH, Jacobianos lineal/angular, rangos, derivación simbólica, unidades y convergencia.
- Error máximo de velocidad de aproximadamente `3.99e-7 m/s` con paso de `0.01 s`.
- Datos dummy: 500 muestras con ruido gaussiano diseñado de `2 mm` por eje; no son mediciones reales.
- Falta completar inversa, estudio de singularidades de Renzo, control de Kenny e integración grupal.

## Informe y revisión

El trabajo es grupal. Se conservan cinco espacios de apreciación individual y uno conjunto. No existe una plantilla adicional impuesta; se siguen la estructura de la consigna y referencias APA. Entrega prevista la próxima semana, sin día exacto confirmado.

El logo se puede colocar en [`assets/branding/`](assets/branding/README.md). La plantilla LaTeX no incorpora automáticamente el borrador diferencial. Markdown sirve para comprender e iterar; PDF y diapositivas se exportan cuando sean útiles.

Las ramas de trabajo abren PR hacia `develop`; `main` conserva la base aceptada. El bootstrap sólo inicializa el repositorio. **El agente llega a Review. Sólo Jairzinho integra PRs, cierra issues y mueve tarjetas a Done.** Las automatizaciones de estado del tablero están desactivadas.
