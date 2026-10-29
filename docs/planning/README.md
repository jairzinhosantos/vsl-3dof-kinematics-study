# Team backlog

El [tablero de GitHub](https://github.com/users/jairzinhosantos/projects/4) contiene el estado vivo. `tasks.json` conserva el plan inicial; no se interpreta como un espejo automático del avance. `github-items.json` relaciona los identificadores con las issues.

- [foundation](https://github.com/jairzinhosantos/vsl-3dof-kinematics-study/issues/1)
- [scope](https://github.com/jairzinhosantos/vsl-3dof-kinematics-study/issues/2)
- [forward](https://github.com/jairzinhosantos/vsl-3dof-kinematics-study/issues/3)
- [inverse](https://github.com/jairzinhosantos/vsl-3dof-kinematics-study/issues/4)
- [differential](https://github.com/jairzinhosantos/vsl-3dof-kinematics-study/issues/5)
- [singularities](https://github.com/jairzinhosantos/vsl-3dof-kinematics-study/issues/6)
- [control](https://github.com/jairzinhosantos/vsl-3dof-kinematics-study/issues/7)
- [simulation](https://github.com/jairzinhosantos/vsl-3dof-kinematics-study/issues/8)
- [paper-audit](https://github.com/jairzinhosantos/vsl-3dof-kinematics-study/issues/9)
- [report](https://github.com/jairzinhosantos/vsl-3dof-kinematics-study/issues/10)
- [presentation](https://github.com/jairzinhosantos/vsl-3dof-kinematics-study/issues/11)

`python3 scripts/sync_github_board.py` muestra el plan sin cambios externos. `--apply` crea sólo las issues ausentes y añade tarjetas nuevas; no sobreescribe el estado de tarjetas existentes ni asigna Done. No se ejecuta en CI ni como automatización.
