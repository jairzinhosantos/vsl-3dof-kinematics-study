"""Ejecuta cada notebook con un kernel nuevo; --save guarda salidas para lectura."""
from pathlib import Path
import argparse
import json
import os
import sys
import tempfile

import nbformat
from nbclient import NotebookClient
from jupyter_client import KernelManager
from jupyter_client.kernelspec import KernelSpecManager

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--save', action='store_true', help='Actualiza las salidas de los notebooks')
    args = parser.parse_args()
    paths = sorted((ROOT / 'notebooks').glob('*/study.ipynb'))
    if not paths:
        raise SystemExit('No se encontraron notebooks')
    # Kernel temporal: usa este entorno Python sin registrar nada en el equipo.
    with tempfile.TemporaryDirectory(prefix='robotics-kernel-') as directory:
        kernel = Path(directory) / 'study'
        kernel.mkdir()
        (kernel / 'kernel.json').write_text(json.dumps({
            'argv': [sys.executable, '-m', 'ipykernel_launcher', '-f', '{connection_file}'],
            'display_name': 'Robotics study', 'language': 'python',
        }))
        for path in paths:
            notebook = nbformat.read(path, as_version=4)
            nbformat.validate(notebook)
            for cell in notebook.cells:
                if cell.cell_type == 'code':
                    cell.outputs = []
                    cell.execution_count = None
            manager = KernelManager(kernel_name='study', kernel_spec_manager=KernelSpecManager(kernel_dirs=[directory]))
            client = NotebookClient(notebook, km=manager, timeout=120, allow_errors=False,
                                    record_timing=False, resources={'metadata': {'path': str(path.parent)}})
            environment = os.environ.copy()
            environment['MPLBACKEND'] = 'module://matplotlib_inline.backend_inline'
            client.execute(cleanup_kc=True, env=environment)
            if args.save:
                nbformat.write(notebook, path)
            print(f'OK: {path.relative_to(ROOT)}', flush=True)
    print(f'{len(paths)} notebooks ejecutados desde cero.')


if __name__ == '__main__':
    main()
