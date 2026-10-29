"""Ejecutar con Blender --background --python este_archivo -- [opciones]."""
from pathlib import Path
import argparse, hashlib, json, sys
import bpy
from mathutils import Vector

ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--motion',default=str(ROOT/'simulations/differential/results/run-001/motion.json'))
parser.add_argument('--output')
parser.add_argument('--render-preview',action='store_true')
args=parser.parse_args(sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else [])
source=Path(args.motion);data=json.loads(source.read_text());out=Path(args.output) if args.output else source.parent/'blender';out.mkdir(parents=True,exist_ok=False)
if data['units']!='m':raise ValueError('Se esperan metros')
bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
scene=bpy.context.scene;scene.unit_settings.system='METRIC';scene.unit_settings.scale_length=1
scene.render.engine='CYCLES';scene.cycles.samples=24;scene.cycles.device='CPU'
scene.render.resolution_x=960;scene.render.resolution_y=720;scene.render.resolution_percentage=100
scene.render.image_settings.file_format='PNG';scene.render.fps=data['fps'];scene.frame_end=len(data['frames'])
scene.world.color=(.18,.18,.18)

def material(name,color,metallic=0):
    mat=bpy.data.materials.new(name);mat.diffuse_color=(*color,1);mat.use_nodes=True
    bs=mat.node_tree.nodes.get('Principled BSDF');bs.inputs['Base Color'].default_value=(*color,1);bs.inputs['Metallic'].default_value=metallic;bs.inputs['Roughness'].default_value=.32
    return mat
navy=material('Base and joints',(.05,.12,.2),.35);teal=material('Links',(.02,.48,.49),.4);gold=material('End effector',(.9,.4,.06),.3)

def ball(name,point,radius,mat):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=24,ring_count=12,radius=radius,location=point)
    obj=bpy.context.object;obj.name=name;obj.data.materials.append(mat);return obj

def position_link(obj,a,b):
    a,b=Vector(a),Vector(b);direction=b-a
    obj.location=(a+b)/2;obj.rotation_quaternion=direction.to_track_quat('Z','Y');obj.scale=(1,1,direction.length)

links=[]
for i in range(3):
    bpy.ops.mesh.primitive_cylinder_add(vertices=32,radius=.012 if i else .02,depth=1)
    obj=bpy.context.object;obj.name=f'Link_{i+1}';obj.rotation_mode='QUATERNION';obj.data.materials.append(teal if i else navy);links.append(obj)
joints=[ball(f'Joint_{i}',[0,0,0],.02,navy if i<3 else gold) for i in range(4)]
# Poses en cada frame, procedentes del mismo modelo matemático de Python.
max_length_error=0.
for frame,row in enumerate(data['frames'],1):
    pts=row['points_m']
    for i,obj in enumerate(joints):
        obj.location=pts[i];obj.keyframe_insert(data_path='location',frame=frame)
    for i,obj in enumerate(links):
        position_link(obj,pts[i],pts[i+1]);max_length_error=max(max_length_error,abs(obj.scale.z-[.04,.29,.24][i]))
        for prop in ['location','rotation_quaternion','scale']:obj.keyframe_insert(data_path=prop,frame=frame)
# Trayectoria del efector como curva de referencia.
curve=bpy.data.curves.new('Synthetic path','CURVE');curve.dimensions='3D';curve.bevel_depth=.0015
poly=curve.splines.new('POLY');poly.points.add(len(data['frames'])-1)
for p,row in zip(poly.points,data['frames']):p.co=(*row['points_m'][-1],1)
obj=bpy.data.objects.new('Synthetic path',curve);scene.collection.objects.link(obj);curve.materials.append(gold)
bpy.ops.mesh.primitive_plane_add(size=2,location=(.2,.1,-.025));floor=bpy.context.object;floor.name='Ground';floor.data.materials.append(material('Ground material',(.65,.68,.71)))
bpy.ops.object.light_add(type='AREA',location=(.2,-.4,1.4));bpy.context.object.data.energy=120;bpy.context.object.data.shape='DISK';bpy.context.object.data.size=1.3
bpy.ops.object.camera_add(location=(1.05,-1.15,.85));camera=bpy.context.object;camera.rotation_euler=(Vector((.23,.12,.15))-camera.location).to_track_quat('-Z','Y').to_euler();camera.data.type='ORTHO';camera.data.ortho_scale=.9;scene.camera=camera
scene['provenance']='Kinematic visualization. Synthetic prescribed motion. No flexible dynamics.'
scene.frame_set(60)
bpy.ops.wm.save_as_mainfile(filepath=str(out/'vsl-3dof-study.blend'))
if args.render_preview:
    scene.render.filepath=str(out/'robot-preview.png');bpy.ops.render.render(write_still=True)
(out/'manifest.json').write_text(json.dumps({'blender_version':bpy.app.version_string,'input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'frames':len(data['frames']),'fps':data['fps'],'units':'m','max_link_length_error_m':max_length_error,'kind':'kinematic_visualization','physical_validation':False},indent=2)+'\n')
print('BLENDER_SCENE_READY',out)
