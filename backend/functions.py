# funciones para crear y verificar tokens
# tokens para admin y usuarios

from flask import jsonify, request
import bcrypt
from models import Usuario, LogoutToken, db
import datetime
import os
import jwt
from functools import wraps

def login_check(data):
    if not data or not data['correo'] or not data['contraseña']:
        return jsonify({'message':'Faltan datos'}), 400
    usuario = Usuario.query.filter_by(correo=data['correo']).first()
    if not usuario:
        return jsonify({'message':'Usuario no encontrado'}), 404
    if bcrypt.checkpw(data['contraseña'].encode('utf-8'), usuario.contraseña.encode('utf-8')):
        token = jwt.encode({'id':usuario.id,'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=30)},os.environ['SECRET_KEY'])
        db.session.add(LogoutToken(token, datetime.datetime.utcnow()))
        db.session.commit()
        return jsonify({'token':token})
    else:
        return jsonify({'message':'Contraseña incorrecta'}), 401
    
def blacklist_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        blocked_token = None
        if 'x-auth-token' in request.headers:
            blocked_token = request.headers['x-auth-token']
        if not blocked_token:
            return jsonify({'message':'Token no encontrado'}), 404
        try:
            blocked = LogoutToken(blocked_token,datetime.datetime.utcnow()).first()
            db.session.add(blocked)
            db.session.commit()
            return f(*args, **kwargs)
        except Exception as e:
            return jsonify({'message':'Token inválido'}), 401
    return decorated

def admin_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-auth-token' in request.headers:
            token = request.headers['x-auth-token']
        if not token:
            return jsonify({'message':'Token no encontrado'}), 404
        blocked_tokens = LogoutToken.query.filter_by(token=token).all()
        if blocked_tokens:
            return jsonify({'message':'No has iniciado sesion'}), 401
        try:
            data = jwt.decode(token, os.environ['SECRET_KEY'])
            current_user = Usuario.query.get(data['id'])
            if current_user.es_admin:
                return f(*args, **kwargs)
            else:
                return jsonify({'message':'No tienes permisos para realizar esta acción'}), 403
        except Exception as e:
            return jsonify({'message':'Token inválido'}), 401
    return decorated

def user_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-auth-token' in request.headers:
            token = request.headers['x-auth-token']
        if not token:
            return jsonify({'message':'Token no encontrado'}), 404
        blocked_tokens = LogoutToken.query.filter_by(token=token).all()
        if blocked_tokens:
            return jsonify({'message':'No has iniciado sesion'}), 401
        try:
            data = jwt.decode(token, os.environ['SECRET_KEY'])
            current_user = Usuario.query.get(data['id'])
            return f(*args, **kwargs)
        except Exception as e:
            return jsonify({'message':'Token inválido'}), 401
    return decorated
