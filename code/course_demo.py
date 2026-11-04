"""Produce las comprobaciones y figuras de los métodos vistos en clase."""
from pathlib import Path
import argparse,csv,hashlib,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from course import geometric_position,homogeneous,inverse_position,polynomial,control,cartesian_reference
from model import forward,joint_points,jacobian
ROOT=Path(__file__).resolve().parents[1]

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def csvfile(path,header,rows):
    with path.open('w',newline='') as f:
        w=csv.writer(f);w.writerow(header);w.writerows(rows)

def control_metrics(result):
    norm=np.linalg.norm(result['error'],axis=1)
    tail=result['t']>=result['t'][-1]/2
    return dict(initial_error_m=float(norm[0]),final_error_m=float(norm[-1]),rmse_m=float(np.sqrt(np.mean(norm**2))),tail_rmse_m=float(np.sqrt(np.mean(norm[tail]**2))),min_sigma_m_rad=float(result['sigma'].min()),max_abs_joint_rate_rad_s=float(abs(result['dq']).max()))

def run(run_id):
    if not run_id.replace('-','').replace('_','').isalnum():raise ValueError('run-id inválido')
    cfgpath=ROOT/'simulations/course/config.json';cfg=json.loads(cfgpath.read_text());L=cfg['lengths_m']
    out=cfgpath.parent/'results'/run_id;out.mkdir(parents=True,exist_ok=False)
    q0=np.deg2rad(cfg['example_q_deg']);qf=np.deg2rad(cfg['final_q_deg'])
    T=forward(q0,L)[0];M=homogeneous(q0,L);p=geometric_position(q0,L)
    inverse=inverse_position(p,L)
    residuals=[float(np.linalg.norm(forward(q,L)[0][:3,3]-p)) for q in inverse]
    csvfile(out/'inverse.csv',['q1_rad','q2_rad','q3_rad','residual_m'],np.column_stack([inverse,residuals]))
    grid=np.meshgrid(*[np.deg2rad(np.linspace(*limits,cfg['workspace_samples_per_joint'])) for limits in cfg['workspace_ranges_deg']],indexing='ij')
    sampled=np.column_stack([g.ravel() for g in grid]);points=np.array([geometric_position(q,L) for q in sampled])
    fig=plt.figure(figsize=(10,4.5),layout='constrained');ax=fig.add_subplot(121,projection='3d');arm=joint_points(q0,L)
    ax.plot(*arm.T,'o-',lw=4,color='#007f82')
    for i,point in enumerate(arm):ax.text(*point,f'  O{i}')
    ax.set(xlabel='x (m)',ylabel='y (m)',zlabel='z (m)',title='Geometría nominal · ejemplo 30°, 40°, −50°');ax.set(xlim=(-.03,.55),ylim=(-.05,.35),zlim=(0,.4));ax.set_box_aspect([.58,.4,.4])
    from matplotlib.ticker import MaxNLocator
    for axis in [ax.xaxis,ax.yaxis,ax.zaxis]:axis.set_major_locator(MaxNLocator(4))
    ax=fig.add_subplot(122,projection='3d');ax.scatter(*points.T,s=1.5,alpha=.45,color='#17324d');ax.set(xlabel='x (m)',ylabel='y (m)',zlabel='z (m)',title='Espacio muestreado · rangos ilustrativos');ax.set_box_aspect([1,1,1]);fig.savefig(out/'workspace.png',dpi=170);plt.close(fig)
    duration=cfg['interpolation_duration_s'];t=np.linspace(0,duration,round(duration/cfg['interpolation_dt_s'])+1)
    fig,axes=plt.subplots(3,3,figsize=(10,7),layout='constrained')
    endpoints={}
    for order in [3,5]:
        q,v,a=polynomial(q0,qf,t,duration,order)
        csvfile(out/f'polynomial-{order}.csv',['t_s',*[f'q{i}_rad' for i in range(1,4)],*[f'dq{i}_rad_s' for i in range(1,4)],*[f'ddq{i}_rad_s2' for i in range(1,4)]],np.column_stack([t,q,v,a]))
        endpoints[str(order)]={'max_endpoint_velocity_rad_s':float(abs(v[[0,-1]]).max()),'max_endpoint_acceleration_rad_s2':float(abs(a[[0,-1]]).max())}
        for row,(values,label) in enumerate([(q,'q (rad)'),(v,'dq/dt (rad/s)'),(a,'d²q/dt² (rad/s²)')]):
            for col in range(3):axes[row,col].plot(t,values[:,col],label=f'Orden {order}');axes[row,col].set(xlabel='t (s)',ylabel=label);axes[row,col].grid(alpha=.2)
    for j in range(3):axes[0,j].set_title(f'Articulación {j+1}');axes[0,j].legend()
    fig.savefig(out/'interpolation.png',dpi=170);plt.close(fig)
    goal=geometric_position(cfg['position_target_q_rad'],L)
    position=control(cfg['position_q0_rad'],cfg['position_duration_s'],cfg['dt_s'],cfg['gain_per_s'],goal,L)
    qtrack=inverse_position(cartesian_reference(0.)[0],L)[-1]+cfg['tracking_initial_offset_rad']
    tracking=control(qtrack,cfg['tracking_duration_s'],cfg['dt_s'],cfg['gain_per_s'],lengths=L)
    fine=control(qtrack,cfg['tracking_duration_s'],cfg['dt_s']/2,cfg['gain_per_s'],lengths=L)
    stress=control([0,0,0],duration=1.,dt=.1,target=[.5,0,.04],lengths=L)
    for name,result in [('position',position),('tracking',tracking)]:
        csvfile(out/f'{name}.csv',['t_s','q1_rad','q2_rad','q3_rad','x_m','y_m','z_m','xd_m','yd_m','zd_m','ex_m','ey_m','ez_m','sigma_min_m_rad'],np.column_stack([result['t'],result['q'],result['p'],result['desired'],result['error'],result['sigma']]))
        csvfile(out/f'{name}-commands.csv',['t_s','dq1_rad_s','dq2_rad_s','dq3_rad_s'],np.column_stack([result['t'][:-1],result['dq']]))
    fig,axes=plt.subplots(2,2,figsize=(10,6),layout='constrained')
    for j,(name,result) in enumerate([('Posición',position),('Seguimiento',tracking)]):
        axes[0,j].plot(result['t'],result['error']*1000);axes[0,j].set(title=name,xlabel='t (s)',ylabel='Error por eje (mm)');axes[0,j].legend(['x','y','z'])
        axes[1,j].plot(result['t'][:-1],result['dq']);axes[1,j].set(xlabel='t (s)',ylabel='Velocidad articular (rad/s)');axes[1,j].legend(['q1','q2','q3'])
    for ax in axes.flat:ax.grid(alpha=.2)
    fig.savefig(out/'control.png',dpi=170);plt.close(fig)
    fig=plt.figure(figsize=(6,5),layout='constrained');ax=fig.add_subplot(111,projection='3d');ax.plot(*tracking['desired'].T,label='Deseada');ax.plot(*tracking['p'].T,'--',label='Obtenida');ax.set(xlabel='x (m)',ylabel='y (m)',zlabel='z (m)',title='Seguimiento cartesiano');ax.legend();fig.savefig(out/'tracking.png',dpi=170);plt.close(fig)
    ranks=[]
    for name,q in [('regular',q0),('elbow',[0,0,0]),('intersection',[0,np.pi/2,0])]:
        JL,_,J=jacobian(q,L);ranks.append(dict(case=name,rank_JL=int(np.linalg.matrix_rank(JL,tol=1e-10)),rank_J=int(np.linalg.matrix_rank(J,tol=1e-10)),det_JL=float(np.linalg.det(JL))))
    metrics=dict(direct_residual_m=float(np.linalg.norm(T[:3,3]-p)),mth_residual=float(abs(T-M).max()),inverse_residuals_m=residuals,workspace_samples=len(points),interpolation=endpoints,position=control_metrics(position),tracking=control_metrics(tracking),tracking_half_step=control_metrics(fine),singular_control=control_metrics(stress),ranks=ranks)
    checks={'direct':metrics['direct_residual_m']<1e-12,'inverse':max(residuals)<1e-12,'position':metrics['position']['final_error_m']<2e-5,'tracking_step':metrics['tracking_half_step']['tail_rmse_m']<.6*metrics['tracking']['tail_rmse_m']}
    (out/'metrics.json').write_text(json.dumps(metrics,indent=2)+'\n')
    inputs=[cfgpath,*[ROOT/'code'/n for n in ['model.py','course.py','course_demo.py']]]
    manifest={'physical_measurements':False,'config':cfg,'checks':checks,'source_sha256':{str(p.relative_to(ROOT)):sha(p) for p in inputs},'output_sha256':{p.name:sha(p) for p in out.iterdir() if p.is_file()},'status':'Review'}
    (out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps(metrics,indent=2))
    if not all(checks.values()):raise RuntimeError('Falló una comprobación de curso')

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--run-id',required=True);run(parser.parse_args().run_id)
