### Prueba técnica de backend ###

# instalaciones requeridas en entorno virtual:
# pip install flask flask_sqlalchemy flask_cors
# pip install psycopg2
# pip install bcrypt
# pip install pyjwt
# pip install python-dotenv

# Imports
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import Usuario, Tarea, Estado, Proyecto, UsuarioTarea, LogoutToken, db
import bcrypt
from functions import login_check, blacklist_token
from dotenv import load_dotenv
load_dotenv('.env')

# Estados para insertar en caso de no existir
lista_estados = ["pendiente","en progreso","completada"]

# App
app = Flask(__name__)
CORS(app)

# Base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/gestion_tareas'

# Init db
db.init_app(app)

# Agregar datos iniciales
with app.app_context():
    # Crear estados si no existen
    for estado in lista_estados:
        if not Estado.query.filter_by(nombre=estado).first():
            db.session.add(Estado(estado))
            db.session.commit()
    # Crear primer usuario si no existe
    if not Usuario.query.filter_by(correo="admin@admin.com").first():
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw("admin".encode('utf-8'), salt)
        db.session.add(Usuario("admin@admin.com",hashed.decode('utf-8'),True))
        db.session.commit()


# Ruta de prueba, verificar que estén los estados:
#  1: pendiente, 2: en progreso, 3: completada
@app.route('/api/estados', methods=['GET'])
def get_estados():
    estados = Estado.query.all()
    estados_json = [estado.to_JSON() for estado in estados]
    return jsonify(estados_json)

################# Modulo de autenticación #################

# Ruta para iniciar sesión
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    return login_check(data)


# Ruta para cerrar sesión
@app.route('/api/logout', methods=['POST'])
@blacklist_token
def logout():
    return jsonify({'message':'Sesión cerrada'})


################# Modulo de usuarios #################

# Ruta para obtener todos los usuarios
@app.route('/api/usuarios',methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    usuarios_json = [usuario.to_JSON() for usuario in usuarios]
    return jsonify(usuarios_json)

# Ruta para obtener un usuario por id
@app.route('/api/usuarios/<id>',methods=['GET'])
def get_usuario_by_id(id):
    usuario = Usuario.query.get(id)
    usuario_json = usuario.to_JSON()
    return jsonify(usuario_json)

# Ruta para crear un usuario
@app.route('/api/usuarios', methods=['POST'])
def create_usuario():
    data = request.get_json()
    hashed = bcrypt.hashpw(data['contraseña'].encode('utf-8'), bcrypt.gensalt())
    usuario = Usuario(data['correo'],hashed.decode('utf-8'))
    db.session.add(usuario)
    db.session.commit()
    return jsonify({'message':'Usuario creado', 'usuario':usuario.to_JSON()})

# Ruta para eliminar un usuario
@app.route('/api/usuarios/<id>',methods=['DELETE'])
def delete_usuario(id):
    usuario = Usuario.query.get(id)
    if usuario.es_admin:
        return jsonify({'message':'No se puede eliminar el usuario administrador'})
    usuario_tareas = UsuarioTarea.query.filter_by(usuario_id=id).all()
    for usuario_tarea in usuario_tareas:
        db.session.delete(usuario_tarea)
    usuario = Usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'message':'Usuario eliminado'})

################# Modulo de tareas #################

# Ruta para obtener todas las tareas
@app.route('/api/tareas',methods=['GET'])
def get_tareas():
    tareas = Tarea.query.all()
    tareas_json = [tarea.to_JSON() for tarea in tareas]
    return jsonify(tareas_json)

# Ruta para obtener una tarea por id
@app.route('/api/tareas/<id>',methods=['GET'])
def get_tarea_by_id(id):
    tarea = Tarea.query.get(id)
    tarea_json = tarea.to_JSON()
    return jsonify(tarea_json)

# Ruta para crear una tarea
@app.route('/api/tareas', methods=['POST'])
def create_tarea():
    data = request.get_json()
    tarea = Tarea(data['titulo'],data['descripcion'],data['fecha_venc'],data['estado_id'],data['proyecto_id'])
    db.session.add(tarea)
    db.session.commit()
    return jsonify({'message':'Tarea creada', 'tarea':tarea.to_JSON()})

# Ruta para eliminar una tarea
@app.route('/api/tareas/<id>',methods=['DELETE'])
def delete_tarea(id):
    # Eliminar registros de la tabla intermedia (usuarios_tareas)
    usuarios_tareas = UsuarioTarea.query.filter_by(tarea_id=id).all()
    for usuario_tarea in usuarios_tareas:
        db.session.delete(usuario_tarea)
    tarea = Tarea.query.get(id)
    db.session.delete(tarea)
    db.session.commit()
    return jsonify({'message':'Tarea eliminada'})

# Ruta para actualizar una tarea
@app.route('/api/tareas/<id>',methods=['PUT'])
def update_tarea(id):
    data = request.get_json()
    tarea = Tarea.query.get(id)
    tarea.titulo = data['titulo']
    tarea.descripcion = data['descripcion']
    tarea.fecha_venc = data['fecha_venc']
    tarea.estado_id = data['estado_id']
    tarea.proyecto_id = data['proyecto_id']
    db.session.commit()
    return jsonify({'message':'Tarea actualizada'})

# Ruta para actualizar una tarea a estado "completada"
@app.route('/api/tareas/<id>_ok',methods=['PUT'])
def update_tarea_ok(id):
    tarea = Tarea.query.get(id)
    tarea.estado_id = 3
    db.session.commit()
    return jsonify({'message':'Tarea actualizada: completada'})


################# Modulo de proyectos #################

# Ruta para obtener todos los proyectos
@app.route('/api/proyectos',methods=['GET'])
def get_proyectos():
    proyectos = Proyecto.query.all()
    proyectos_json = [proyecto.to_JSON() for proyecto in proyectos]
    return jsonify(proyectos_json)

# Ruta para obtener un proyecto por id
@app.route('/api/proyectos/<id>',methods=['GET'])
def get_proyecto_by_id(id):
    proyecto = Proyecto.query.get(id)
    proyecto_json = proyecto.to_JSON()
    return jsonify(proyecto_json)

# Ruta para crear un proyecto
@app.route('/api/proyectos', methods=['POST'])
def create_proyecto():
    data = request.get_json()
    proyecto = Proyecto(data['titulo'],data['descripcion'])
    db.session.add(proyecto)
    db.session.commit()
    return jsonify({'message':'Proyecto creado', 'proyecto':proyecto.to_JSON()})

# Ruta para eliminar un proyecto
@app.route('/api/proyectos/<id>',methods=['DELETE'])
def delete_proyecto(id):
    # Eliminar tareas de usuarios asociadas al proyecto
    tareas = Tarea.query.filter_by(proyecto_id=id).all()
    for tarea in tareas:
        usuarios_tareas = UsuarioTarea.query.filter_by(tarea_id=tarea.id).all()
        for usuario_tarea in usuarios_tareas:
            db.session.delete(usuario_tarea)
        db.session.commit()
        db.session.delete(tarea)
    proyecto = Proyecto.query.get(id)
    db.session.delete(proyecto)
    db.session.commit()
    return jsonify({'message':'Proyecto eliminado'})

# Ruta para actualizar un proyecto
@app.route('/api/proyectos/<id>',methods=['PUT'])
def update_proyecto(id):
    data = request.get_json()
    proyecto = Proyecto.query.get(id)
    proyecto.titulo = data['titulo']
    proyecto.descripcion = data['descripcion']
    db.session.commit()
    return jsonify({'message':'Proyecto actualizado'})

# Ruta para obtener las tareas de un proyecto
@app.route('/api/proyectos/<id>_tareas',methods=['GET'])
def get_proyecto_tareas(id):
    tareas = Tarea.query.filter_by(proyecto_id=id).all()
    tareas_json = [tarea.to_JSON() for tarea in tareas]
    return jsonify(tareas_json)

################# Modulo de usuarios_tareas #################

# Ruta para obtener todas las asociaciones de usuarios_tareas
@app.route('/api/usuarios_tareas',methods=['GET'])
def get_usuarios_tareas():
    usuarios_tareas = UsuarioTarea.query.all()
    usuarios_tareas_json = [usuario_tarea.to_JSON() for usuario_tarea in usuarios_tareas]
    return jsonify(usuarios_tareas_json)

# Ruta para obtener todas las tareas asociadas a un usuario
@app.route('/api/usuarios_tareas/<usuario_id>',methods=['GET'])
def get_usuarios_tareas_by_usuario_id(usuario_id):
    usuarios_tareas = UsuarioTarea.query.filter_by(usuario_id=usuario_id).all()
    body = []
    for usuario_tarea in usuarios_tareas:
        id = usuario_tarea.id
        tarea = Tarea.query.get(usuario_tarea.tarea_id)
        body.append({'id':id,'tarea':tarea.to_JSON()})
    return jsonify(body)

# Ruta para obtener todas las tareas asignadas a un usuario (sin completar)
@app.route('/api/usuarios_tareas/<usuario_id>_asignadas',methods=['GET'])
def get_usuarios_tareas_asignadas(usuario_id):
    usuarios_tareas = UsuarioTarea.query.filter_by(usuario_id=usuario_id).all()
    body = []
    for usuario_tarea in usuarios_tareas:
        tarea = Tarea.query.get(usuario_tarea.tarea_id)
        if tarea.estado_id == 1 or tarea.estado_id == 2:
            id = usuario_tarea.id
            body.append({'id':id,'tarea':tarea.to_JSON()})
    return jsonify(body)


# Ruta para crear una asociacion de usuario-tarea
@app.route('/api/usuarios_tareas', methods=['POST'])
def create_usuario_tarea():
    data = request.get_json()
    if UsuarioTarea.query.filter_by(usuario_id=data['usuario_id'],tarea_id=data['tarea_id']).first():
        return jsonify({'message':'Usuario-tarea ya existe'}), 400
    usuario_tarea = UsuarioTarea(data['usuario_id'],data['tarea_id'])
    db.session.add(usuario_tarea)
    db.session.commit()
    return jsonify({'message':'Usuario-tarea creado', 'usuario_tarea':usuario_tarea.to_JSON()})

# Ruta para eliminar una asociacion de usuario-tarea
@app.route('/api/usuarios_tareas/<id>',methods=['DELETE'])
def delete_usuario_tarea(id):
    usuario_tarea = UsuarioTarea.query.get(id)
    db.session.delete(usuario_tarea)
    db.session.commit()
    return jsonify({'message':'Usuario-tarea eliminado'})



################# Correr aplicacion #################
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)