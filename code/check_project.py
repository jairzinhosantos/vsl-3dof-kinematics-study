"""Valida enlaces locales, procedencia de evidencias y política básica de CI."""
from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
IGNORE={'.git','.venv','_local','outputs','output','__pycache__','.pytest_cache','build'}
errors=[];docs=0
for p in ROOT.rglob('*.md'):
    if any(part in IGNORE for part in p.relative_to(ROOT).parts):continue
    docs+=1
    for raw in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',p.read_text()):
        target=raw.split('#')[0].split(' "')[0].strip('<>')
        if not target or re.match(r'^[a-zA-Z]+:',target):continue
        if not (p.parent/target).exists():errors.append(f'Enlace roto: {p.relative_to(ROOT)} -> {target}')
for p in ROOT.glob('simulations/*/results/*/manifest.json'):
    d=json.loads(p.read_text())
    if d.get('physical_measurements') is not False:errors.append(f'Falta etiqueta sintética: {p}')
    for name,digest in d.get('output_sha256',{}).items():
        artifact=p.parent/name
        if not artifact.exists() or hashlib.sha256(artifact.read_bytes()).hexdigest()!=digest:errors.append(f'Evidencia alterada: {artifact}')
# Los notebooks publicados deben poder leerse con salidas completas y sin errores.
for p in ROOT.glob('notebooks/*/study.ipynb'):
    notebook = json.loads(p.read_text())
    cells = [cell for cell in notebook['cells'] if cell['cell_type'] == 'code']
    counts = [cell.get('execution_count') for cell in cells]
    if counts != list(range(1, len(cells) + 1)):
        errors.append(f'Notebook sin ejecución completa y ordenada: {p.relative_to(ROOT)}')
    if any(output.get('output_type') == 'error' for cell in cells for output in cell.get('outputs', [])):
        errors.append(f'Notebook con errores guardados: {p.relative_to(ROOT)}')
    for cell in notebook['cells']:
        if cell['cell_type'] != 'markdown':continue
        source = cell['source']
        if isinstance(source, list):source = ''.join(source)
        for raw in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', source):
            target = raw.split('#')[0].strip('<>')
            if target and not re.match(r'^[a-zA-Z]+:', target) and not (p.parent/target).exists():
                errors.append(f'Enlace roto en notebook: {p.relative_to(ROOT)} -> {target}')
for p in ROOT.glob('.github/workflows/*'):
    text=p.read_text()
    if 'contents: read' not in text:errors.append('CI debe declarar permisos de sólo lectura')
    if re.search(r'(issues: write|pull-requests: write|auto-merge|gh issue close)',text):errors.append('Automatización incompatible con revisión humana')
# El repositorio entrega el PDF listo; el CI comprueba que corresponde a sus fuentes.
build_path=ROOT/'report/output/build.json'
if not build_path.exists():
    errors.append('Falta el PDF preparado y su registro de compilación')
else:
    record=json.loads(build_path.read_text())
    for rel,digest in {record['pdf']:record['pdf_sha256'],**record['source_sha256']}.items():
        p=ROOT/rel
        if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest()!=digest:
            errors.append(f'PDF o fuente modificada sin recompilar: {rel}')
if errors:raise SystemExit('\n'.join(errors))
print(f'OK: {docs} Markdown; enlaces locales, hashes de evidencia y política de revisión.')
