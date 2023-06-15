import json
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer,primary_key=True)
    correo = db.Column(db.String(50),nullable=False)
    contraseña = db.Column(db.String(72),nullable=True)
    
    def __init__(self,correo,contraseña):
        self.correo=correo
        self.contraseña=contraseña
   
    def __repr__(self):
        return '<Usuario %r>' %self.correo
    
    def to_JSON(self):
        return{
            'id':self.id,
            'correo':self.correo,
            'contraseña':self.contraseña
        }
    
class Tarea(db.Model):
    __tablename__ = 'tarea'
    id = db.Column(db.Integer,primary_key=True)
    titulo = db.Column(db.String(50),nullable=False)
    descripcion = db.Column(db.Text,nullable=False)
    fecha_venc = db.Column(db.Date,nullable=False)
    estado_id =db.Column(db.Integer,db.ForeignKey('estado.id'),nullable=False)
    proyecto_id =db.Column(db.Integer,db.ForeignKey('proyecto.id'),nullable=False)

    def __init__(self,titulo,descripcion,fecha_venc,estado_id,proyecto_id):
        self.titulo=titulo
        self.descripcion=descripcion
        self.fecha_venc=fecha_venc
        self.estado_id=estado_id
        self.proyecto_id=proyecto_id

    def __repr__(self):
        return '<Tarea %r>' %self.titulo
    
    def to_JSON(self):
        return{
            'id':self.id,
            'titulo':self.titulo,
            'descripcion':self.descripcion,
            'fecha_venc':self.fecha_venc,
            'estado_id':self.estado_id,
            'proyecto_id':self.proyecto_id
        }

class Estado(db.Model):
    __tablename__ = 'estado'
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(50),nullable=False)

    def __init__(self,nombre):
        self.nombre = nombre
    
    def __repr__(self):
        return '<Estado %r>' %self.nombre
    
    def to_JSON(self):
        return{
            'id':self.id,
            'nombre':self.nombre
        }

class Proyecto(db.Model):
    __tablename__ = 'proyecto'
    id = db.Column(db.Integer,primary_key=True)
    titulo = db.Column(db.String(50),nullable=False)
    descripcion = db.Column(db.Text,nullable=False)

    def __init__(self,titulo,descripcion):
        self.titulo=titulo
        self.descripcion=descripcion

    def __repr__(self):
        return '<Proyecto %r>' %self.titulo
    
    def to_JSON(self):
        return{
            'id':self.id,
            'titulo':self.titulo,
            'descripcion':self.descripcion
        }

class UsuarioTarea(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    usuario_id =db.Column(db.Integer,db.ForeignKey('usuario.id'),nullable=False)
    tarea_id =db.Column(db.Integer,db.ForeignKey('tarea.id'),nullable=False)

    def __init__(self,usuario_id,tarea_id):
        self.usuario_id = usuario_id
        self.tarea_id = tarea_id
    
    def __repr__(self):
        return '<UsuarioTarea %r>' %self.id
    
    def to_JSON(self):
        return{
            'id':self.id,
            'usuario_id':self.usuario_id,
            'tarea_id':self.tarea_id
        }
