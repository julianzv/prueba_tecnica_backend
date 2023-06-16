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
from functions import login_check, blacklist_token, admin_token, user_token
from dotenv import load_dotenv
load_dotenv('.env')

# estados para insertar en caso de no existir
lista_estados = ["pendiente","en progreso","completada"]

# App
app = Flask(__name__)
CORS(app)

# Database
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

# Modulo de autenticación
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    return login_check(data)

@app.route('/api/logout', methods=['POST'])
#@blacklist_token
def logout():
    return jsonify({'message':'Sesión cerrada'})

@app.route('/api/check', methods=['GET'])
#@admin_token
def check():
    return jsonify({'message':'Token válido'})

@app.route('/api/cambiar_contraseña', methods=['POST'])
#@user_token
def cambiar_contraseña():
    data = request.get_json()
    if len(data['contraseña']) < 8:
        return jsonify({'message':'La contraseña debe tener al menos 8 caracteres'})
    usuario = Usuario.query.filter_by(correo=data['correo']).first()
    if usuario:
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(data['contraseña'].encode('utf-8'), salt)
        usuario.contraseña = hashed.decode('utf-8')
        db.session.commit()
        return jsonify({'message':'Contraseña cambiada'})
    else:
        return jsonify({'message':'Usuario no encontrado'})



# Modulo de usuarios
@app.route('/api/usuarios',methods=['GET'])
#@admin_token
def get_usuarios():
    usuarios = Usuario.query.all()
    usuarios_json = [usuario.to_JSON() for usuario in usuarios]
    return jsonify(usuarios_json)

@app.route('/api/usuarios/<id>',methods=['GET'])
def get_usuario_by_id(id):
    usuario = Usuario.query.get(id)
    usuario_json = usuario.to_JSON()
    return jsonify(usuario_json)

@app.route('/api/usuarios', methods=['POST'])
def create_usuario():
    data = request.get_json()
    hashed = bcrypt.hashpw(data['contraseña'].encode('utf-8'), bcrypt.gensalt())
    usuario = Usuario(data['correo'],hashed.decode('utf-8'))
    db.session.add(usuario)
    db.session.commit()
    return jsonify({'message':'Usuario creado'})

@app.route('/api/usuarios/<id>',methods=['DELETE'])
def delete_usuario(id):
    usuario = Usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'message':'Usuario eliminado'})

# Modulo de tareas
@app.route('/api/tareas',methods=['GET'])
def get_tareas():
    tareas = Tarea.query.all()
    tareas_json = [tarea.to_JSON() for tarea in tareas]
    return jsonify(tareas_json)

@app.route('/api/tareas/<id>',methods=['GET'])
def get_tarea_by_id(id):
    tarea = Tarea.query.get(id)
    tarea_json = tarea.to_JSON()
    return jsonify(tarea_json)

@app.route('/api/tareas', methods=['POST'])
def create_tarea():
    data = request.get_json()
    tarea = Tarea(data['titulo'],data['descripcion'],data['fecha_venc'],data['estado_id'],data['proyecto_id'])
    db.session.add(tarea)
    db.session.commit()
    return jsonify({'message':'Tarea creada'})

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

@app.route('/api/tareas/<id>_ok',methods=['PUT'])
def update_tarea_ok(id):
    tarea = Tarea.query.get(id)
    tarea.estado_id = 3
    db.session.commit()
    return jsonify({'message':'Tarea actualizada: completada'})

# Modulo de proyectos
@app.route('/api/proyectos',methods=['GET'])
def get_proyectos():
    proyectos = Proyecto.query.all()
    proyectos_json = [proyecto.to_JSON() for proyecto in proyectos]
    return jsonify(proyectos_json)

@app.route('/api/proyectos/<id>',methods=['GET'])
def get_proyecto_by_id(id):
    proyecto = Proyecto.query.get(id)
    proyecto_json = proyecto.to_JSON()
    return jsonify(proyecto_json)

@app.route('/api/proyectos', methods=['POST'])
def create_proyecto():
    data = request.get_json()
    proyecto = Proyecto(data['titulo'],data['descripcion'])
    db.session.add(proyecto)
    db.session.commit()
    return jsonify({'message':'Proyecto creado'})

@app.route('/api/proyectos/<id>',methods=['DELETE'])
def delete_proyecto(id):
    # Eliminar tareas asociadas al proyecto
    tareas = Tarea.query.filter_by(proyecto_id=id).all()
    for tarea in tareas:
        db.session.delete(tarea)
    proyecto = Proyecto.query.get(id)
    db.session.delete(proyecto)
    db.session.commit()
    return jsonify({'message':'Proyecto eliminado'})

@app.route('/api/proyectos/<id>',methods=['PUT'])
def update_proyecto(id):
    data = request.get_json()
    proyecto = Proyecto.query.get(id)
    proyecto.nombre = data['titulo']
    proyecto.descripcion = data['descripcion']
    db.session.commit()
    return jsonify({'message':'Proyecto actualizado'})

# Modulo de usuarios_tareas
@app.route('/api/usuarios_tareas',methods=['GET'])
def get_usuarios_tareas():
    usuarios_tareas = UsuarioTarea.query.all()
    usuarios_tareas_json = [usuario_tarea.to_JSON() for usuario_tarea in usuarios_tareas]
    return jsonify(usuarios_tareas_json)

@app.route('/api/usuarios_tareas/<usuario_id>',methods=['GET'])
def get_usuarios_tareas_by_usuario_id(usuario_id):
    usuarios_tareas = UsuarioTarea.query.filter_by(usuario_id=usuario_id).all()
    usuarios_tareas_json = [usuario_tarea.to_JSON() for usuario_tarea in usuarios_tareas]
    return jsonify(usuarios_tareas_json)


@app.route('/api/usuarios_tareas', methods=['POST'])
def create_usuario_tarea():
    data = request.get_json()
    usuario_tarea = UsuarioTarea(data['usuario_id'],data['tarea_id'])
    db.session.add(usuario_tarea)
    db.session.commit()
    return jsonify({'message':'Usuario-tarea creado'})

@app.route('/api/usuarios_tareas/<id>',methods=['DELETE'])
def delete_usuario_tarea(id):
    usuario_tarea = UsuarioTarea.query.get(id)
    db.session.delete(usuario_tarea)
    db.session.commit()
    return jsonify({'message':'Usuario-tarea eliminado'})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)