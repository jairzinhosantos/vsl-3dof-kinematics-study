"""Carga idempotente del plan en GitHub. Por defecto sólo muestra el plan."""
from pathlib import Path
import argparse,json,subprocess
ROOT=Path(__file__).resolve().parents[1]
REPO='jairzinhosantos/vsl-3dof-kinematics-study';OWNER='jairzinhosantos';NUMBER='4';PROJECT='PVT_kwHOBKjA8c4BpNta'

def gh(*args):return json.loads(subprocess.check_output(['gh',*args],text=True))
def api(endpoint,payload):
    return json.loads(subprocess.check_output(['gh','api',endpoint,'--input','-'],input=json.dumps(payload),text=True))
def gql(query,variables):
    r=api('graphql',dict(query=query,variables=variables))
    if r.get('errors'):raise RuntimeError(r['errors'])
    return r['data']

def main(apply):
    tasks=json.loads((ROOT/'docs/planning/tasks.json').read_text())
    assert all(t['status'] in ['Backlog','Ready','In Progress','Review'] for t in tasks)
    if not apply:print(json.dumps(tasks,ensure_ascii=False,indent=2));return
    fields=gh('project','field-list',NUMBER,'--owner',OWNER,'--format','json')['fields']
    for name,typ,options in [('Team owner','TEXT',None),('Priority','SINGLE_SELECT','P0,P1,P2')]:
        if not any(f['name']==name for f in fields):
            args=['project','field-create',NUMBER,'--owner',OWNER,'--name',name,'--data-type',typ,'--format','json']
            if options:args+=['--single-select-options',options]
            gh(*args)
    fields={f['name']:f for f in gh('project','field-list',NUMBER,'--owner',OWNER,'--format','json')['fields']}
    issues=gh('api',f'repos/{REPO}/issues?state=all&per_page=100')
    items=gh('project','item-list',NUMBER,'--owner',OWNER,'--limit','100','--format','json')['items']
    mapping=[]
    for task in tasks:
        marker=f"<!-- study-task:{task['id']} -->"
        issue=next((i for i in issues if marker in (i.get('body') or '')),None)
        if issue is None:
            deps=', '.join(task['depends_on']) or 'Sin dependencia técnica previa'
            body=f"{marker}\n## Responsable del equipo\n{task['owner']}\n\n## Dependencias\n{deps}\n\n## Criterios para Review\n"+'\n'.join('- [ ] '+c for c in task['criteria'])+'\n\n## Revisión humana\nEl agente llega a Review. Sólo Jairzinho integra PRs, cierra issues, asigna Completed date y mueve a Done. CI no constituye aceptación.\n'
            payload={'title':task['title'],'body':body}
            if task['owner']=='Jairzinho':payload['assignees']=[OWNER]
            issue=api(f'repos/{REPO}/issues',payload);issues.append(issue)
        if issue['state']!='open':raise RuntimeError('La tarea ya fue cerrada; no se reabre ni altera automáticamente')
        item=next((i for i in items if i.get('content',{}).get('url')==issue['html_url']),None)
        if item is None:
            item=gh('project','item-add',NUMBER,'--owner',OWNER,'--url',issue['html_url'],'--format','json');items.append(item)
            # Estado inicial solamente. Una resincronización no sobrescribe avances humanos.
            for name,value in [('Status',task['status']),('Priority',task['priority'])]:
                field=fields[name];option=next(o['id'] for o in field['options'] if o['name']==value)
                gh('project','item-edit','--id',item['id'],'--project-id',PROJECT,'--field-id',field['id'],'--single-select-option-id',option,'--format','json')
            gh('project','item-edit','--id',item['id'],'--project-id',PROJECT,'--field-id',fields['Team owner']['id'],'--text',task['owner'],'--format','json')
        mapping.append(dict(id=task['id'],issue_number=issue['number'],url=issue['html_url'],item_id=item['id']))
        print(task['id'],issue['html_url'],flush=True)
    (ROOT/'docs/planning/github-items.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2)+'\n')
    gql('mutation($input:UpdateProjectV2Input!){updateProjectV2(input:$input){projectV2{id}}}',{'input':{'projectId':PROJECT,'shortDescription':'Estudio de cinemática en Python · evidencias y revisión humana','readme':'# VSL 3-DOF · MIA UNI Midterm\n\nPython como entorno principal. Markdown para estudiar y Blender para construcción virtual.\n\nBacklog → Ready → In Progress → Review. Sólo Jairzinho acepta, integra, cierra y mueve a Done. Sin automatizaciones de cierre.\n\nAlcance rígido, valoración por construcción y día exacto de entrega pendientes de confirmar.\n\nRepositorio: https://github.com/'+REPO}})
    subprocess.run(['gh','project','link',NUMBER,'--owner',OWNER,'--repo',REPO],check=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--apply',action='store_true');main(parser.parse_args().apply)
