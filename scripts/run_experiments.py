"""Ejecuta dos protocolos acotados y conserva evidencia por run-id."""
from pathlib import Path
import argparse, csv, hashlib, json, platform, subprocess
from datetime import datetime, timezone
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from robotics_study.model import forward
from robotics_study.simulation import simulate
ROOT=Path(__file__).resolve().parents[1]

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write_csv(path,header,rows):
    with path.open('w',newline='') as f:
        writer=csv.writer(f);writer.writerow(header);writer.writerows(rows)

def provenance(config,path):
    sources=[ROOT/'src/robotics_study/model.py',ROOT/'src/robotics_study/simulation.py',Path(__file__),path]
    return {'created_at_utc':datetime.now(timezone.utc).isoformat(),'python':platform.python_version(),'numpy':np.__version__,'config':config,'source_sha256':{str(p.relative_to(ROOT)):sha(p) for p in sources},'status':'Review','physical_measurements':False}

def run(run_id):
    if not run_id.replace('-','').replace('_','').isalnum():raise ValueError('run-id inválido')
    cfg_paths=[ROOT/'simulations'/name/'config.json' for name in ['differential','dummy-sensor']]
    for p in cfg_paths:
        if (p.parent/'results'/run_id).exists():raise FileExistsError('Use otro run-id; se conserva la evidencia existente')
    out=cfg_paths[0].parent/'results'/run_id;out.mkdir(parents=True)
    cfg=json.loads(cfg_paths[0].read_text());s=simulate(cfg['duration_s'],cfg['dt_s'],cfg['lengths_m'])
    header=['t_s','q1_rad','q2_rad','q3_rad','dq1_rad_s','dq2_rad_s','dq3_rad_s','x_m','y_m','z_m','vx_m_s','vy_m_s','vz_m_s','sigma_min_m_rad']
    write_csv(out/'trajectory.csv',header,np.column_stack([s['t'],s['q'],s['dq'],s['p'],s['v'],s['sigma']]))
    # Blender consume exactamente estas posiciones, sin otra implementación de la cinemática.
    frames=[{'t_s':float(s['t'][k]),'points_m':s['points'][k].tolist()} for k in range(0,len(s['t']),5)]
    (out/'motion.json').write_text(json.dumps({'units':'m','fps':20,'data_kind':cfg['data_kind'],'frames':frames},indent=2)+'\n')
    convergence=[{'dt_s':dt,'max_velocity_error_m_s':float(simulate(cfg['duration_s'],dt,cfg['lengths_m'])['error'].max())} for dt in cfg['convergence_dt_s']]
    passed=all(row['max_velocity_error_m_s']<cfg['velocity_tolerance_m_s'] for row in convergence)
    fig,axes=plt.subplots(2,2,figsize=(10,7),layout='constrained')
    for i,label in enumerate(['x','y','z']):axes[0,0].plot(s['t'],s['p'][:,i],label=label);axes[0,1].plot(s['t'],s['v'][:,i],label=label)
    axes[0,0].set(xlabel='t (s)',ylabel='Posición (m)');axes[0,0].legend()
    axes[0,1].set(xlabel='t (s)',ylabel='Velocidad (m/s)');axes[0,1].legend()
    axes[1,0].semilogy(s['t'][1:-1],s['error']);axes[1,0].set(xlabel='t (s)',ylabel='Error de velocidad (m/s)')
    axes[1,1].plot(s['t'],s['sigma']);axes[1,1].set(xlabel='t (s)',ylabel='σ mínimo (m/rad)')
    for ax in axes.flat:ax.grid(alpha=.25)
    fig.suptitle('Movimiento prescrito · datos sintéticos · modelo rígido nominal')
    fig.savefig(out/'diagnostics.png',dpi=160);fig.savefig(out/'diagnostics.svg');plt.close(fig)
    html_dir=ROOT/'outputs'/run_id;html_dir.mkdir(parents=True,exist_ok=True)
    def arm(frame):
        points=np.array(frame['points_m'])
        return go.Scatter3d(x=points[:,0],y=points[:,1],z=points[:,2],mode='lines+markers',line={'width':10,'color':'#007f82'},marker={'size':5},name='Robot nominal')
    fig=go.Figure(data=[arm(frames[0]),go.Scatter3d(x=s['p'][:,0],y=s['p'][:,1],z=s['p'][:,2],mode='lines',name='Trayectoria sintética')],frames=[go.Frame(data=[arm(f)],traces=[0],name=str(i)) for i,f in enumerate(frames)])
    fig.update_layout(title='VSL 3-DOF · movimiento prescrito, sin dinámica flexible',scene={'xaxis':{'title':'x (m)','range':[-.1,.6]},'yaxis':{'title':'y (m)','range':[-.15,.4]},'zaxis':{'title':'z (m)','range':[-.1,.6]},'aspectmode':'data'},updatemenus=[{'buttons':[{'label':'Reproducir','method':'animate','args':[None,{'frame':{'duration':50,'redraw':True},'transition':{'duration':0},'fromcurrent':True}]},{'label':'Pausa','method':'animate','args':[[None],{'mode':'immediate','frame':{'duration':0,'redraw':False}}]}]}],sliders=[{'steps':[{'label':f"{f['t_s']:.1f}",'method':'animate','args':[[str(i)],{'mode':'immediate','frame':{'duration':0,'redraw':True}}]} for i,f in enumerate(frames)],'currentvalue':{'prefix':'t (s): '}}])
    fig.write_html(html_dir/'robot-motion.html',include_plotlyjs=True,auto_play=False)
    report=provenance(cfg,cfg_paths[0]);report.update({'passed':passed,'convergence':convergence,'min_sigma_m_rad':float(s['sigma'].min()),'output_sha256':{p.name:sha(p) for p in out.iterdir() if p.is_file()}})
    (out/'manifest.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
    if not passed:raise RuntimeError('El protocolo de velocidades no pasó')
    # Fixture dummy de sensor: observaciones = verdad nominal + ruido diseñado.
    cfg=json.loads(cfg_paths[1].read_text());out=cfg_paths[1].parent/'results'/run_id;out.mkdir(parents=True)
    rng=np.random.default_rng(cfg['seed']);q=rng.uniform(*cfg['q_range_rad'],(cfg['samples'],3))
    truth=np.array([forward(row)[0][:3,3] for row in q]);noise=rng.normal(0,cfg['noise_std_m'],truth.shape);observed=truth+noise
    write_csv(out/'synthetic-sensor.csv',['q1_rad','q2_rad','q3_rad','true_x_m','true_y_m','true_z_m','dummy_x_m','dummy_y_m','dummy_z_m'],np.column_stack([q,truth,observed]))
    rmse=float(np.sqrt(np.mean(np.sum(noise**2,axis=1))));expected=np.sqrt(3)*cfg['noise_std_m']
    fig,ax=plt.subplots(figsize=(7,4),layout='constrained');ax.hist(np.linalg.norm(noise,axis=1)*1000,bins=30,color='#007f82');ax.set(xlabel='Error de posición diseñado (mm)',ylabel='Muestras',title='Fixture de sensor sintético · no son mediciones reales');fig.savefig(out/'synthetic-error.png',dpi=160);plt.close(fig)
    report=provenance(cfg,cfg_paths[1]);report.update({'rmse_position_m':rmse,'expected_rms_m':expected,'passed_fixture_check':bool(.85*expected<rmse<1.15*expected),'interpretation':'Prueba del flujo de datos; no estima precisión del robot real.','output_sha256':{p.name:sha(p) for p in out.iterdir() if p.is_file()}})
    (out/'manifest.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
    assert report['passed_fixture_check']
    print(json.dumps({'run_id':run_id,'velocity_passed':passed,'dummy_rmse_m':rmse,'interactive':str(html_dir/'robot-motion.html')},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--run-id',required=True);run(parser.parse_args().run_id)
