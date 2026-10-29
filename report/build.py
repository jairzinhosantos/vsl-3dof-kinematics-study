"""Exporta la plantilla grupal cuando se solicita un PDF."""
from pathlib import Path
import shutil
import subprocess
import os
import platform
import tempfile
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = {'report': 'report'}

def compile_projects(env):
    out = ROOT / 'report/output'
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
        inputs = list(project.glob('*.tex')) + list(project.glob('sections/*.tex')) + list(project.glob('*.bib'))
        inputs += [ROOT/'assets/logos/uni-logo.png', ROOT/'simulations/differential/results/run-001/diagnostics.png']
        inputs += list((ROOT/'simulations/course/results/run-001').glob('*.png'))
        inputs += [ROOT/'simulations/course/results/run-001/metrics.json']
        sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
        record = {'pdf': str((out/(name+'.pdf')).relative_to(ROOT)), 'pdf_sha256': sha(out/(name+'.pdf')), 'source_sha256': {str(p.relative_to(ROOT)): sha(p) for p in sorted(inputs)}}
        (out/'build.json').write_text(json.dumps(record,indent=2)+'\n')
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
