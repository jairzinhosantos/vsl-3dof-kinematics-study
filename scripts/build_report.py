"""Exporta la plantilla grupal cuando se solicita un PDF."""
from pathlib import Path
import shutil
import subprocess
import os
import platform
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = {'group-report': 'report'}

def compile_projects(env):
    out = ROOT / 'outputs/report'
    out.mkdir(parents=True, exist_ok=True)
    for name, rel in PROJECTS.items():
        project = ROOT / rel
        build = project/'build'
        build.mkdir(exist_ok=True)
        with (build/'compilation.log').open('w') as log:
            result = subprocess.run(['latexmk','-g','-pdf','-interaction=nonstopmode','-halt-on-error','-outdir=build','main.tex'],cwd=project,stdout=log,stderr=subprocess.STDOUT,env=env)
        if result.returncode:
            raise RuntimeError(f'Fallo LaTeX: {build / "compilation.log"}')
        shutil.copy2(build/'main.pdf', out/(name+'.pdf'))
        print(f'Exportado: {name}.pdf', flush=True)

def main():
    env = os.environ.copy()
    biber = shutil.which('biber')
    if not biber:
        raise RuntimeError('Se requiere biber (incluido en TeX Live/MacTeX).')
    probe = subprocess.run([biber,'--version'],capture_output=True,text=True)
    if probe.returncode and platform.system() == 'Darwin' and shutil.which('lipo'):
        # Algunas instalaciones universales fallan al autoextraer su arquitectura.
        # Usar una copia temporal del binario instalado sin modificar MacTeX.
        with tempfile.TemporaryDirectory(prefix='robotica-biber-') as tmp:
            binary = Path(tmp)/'biber'
            subprocess.run(['lipo',biber,'-thin',platform.machine(),'-output',str(binary)],check=True)
            binary.chmod(0o755)
            subprocess.run([str(binary),'--version'],check=True)
            env['PATH'] = tmp + os.pathsep + env['PATH']
            compile_projects(env)
    elif probe.returncode:
        raise RuntimeError('Biber no funciona: '+probe.stderr)
    else:
        compile_projects(env)

if __name__ == '__main__':
    main()
