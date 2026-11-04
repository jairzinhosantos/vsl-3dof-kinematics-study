"""Punto de entrada del parcial: pruebas, simulación, Blender e informe."""
from pathlib import Path
import argparse
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    commands.add_parser('test', help='Comprueba el modelo y los archivos del proyecto')
    for name, help_text in [('simulate','Simula el movimiento del robot'), ('course','Ejecuta las comprobaciones alineadas al curso'), ('dummy','Genera datos de sensor sintéticos (opcional)'), ('blender','Visualiza una simulación existente en Blender')]:
        cmd = commands.add_parser(name, help=help_text)
        cmd.add_argument('--run-id', required=True, help='Identificador de la ejecución, por ejemplo run-003')
    commands.add_parser('report', help='Exporta el informe a report/output/report.pdf')
    args = parser.parse_args()
    if args.command == 'test':
        calls = [[sys.executable,'-m','pytest','-q'], [sys.executable,'code/check_project.py']]
    elif args.command in ('simulate','dummy'):
        case = 'differential' if args.command == 'simulate' else 'dummy-sensor'
        calls = [[sys.executable,'code/simulate.py','--case',case,'--run-id',args.run_id]]
    elif args.command == 'course':
        calls = [[sys.executable,'code/course_demo.py','--run-id',args.run_id]]
    elif args.command == 'report':
        calls = [[sys.executable,'report/build.py']]
    else:
        if not args.run_id.replace('-','').replace('_','').isalnum():
            parser.error('run-id inválido')
        motion = ROOT/'simulations/differential/results'/args.run_id/'motion.json'
        if not motion.exists():
            parser.error(f'No existe {motion}. Primero se ejecuta simulate con ese run-id.')
        blender = shutil.which('blender')
        if not blender:
            mac = Path('/Applications/Blender.app/Contents/MacOS/Blender')
            if mac.exists():blender = str(mac)
        if not blender:parser.error('Se requiere Blender instalado para esta opción.')
        calls = [[blender,'--background','--factory-startup','--python-exit-code','1','--python',str(ROOT/'code/blender_scene.py'),'--','--motion',str(motion),'--render-preview']]
    for call in calls:
        subprocess.run(call,cwd=ROOT,check=True)

if __name__ == '__main__':
    main()
