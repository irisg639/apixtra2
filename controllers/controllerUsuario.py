from models.usuario import Usuario
from config import db
from flask import jsonify
from flask_jwt_extended import create_access_token

def obtener_todos_los_usuarios():
    try:
        return [user.to_dict() for user in Usuario.query.all()]
    except Exception as e:
        return jsonify({"error": str(e)})

def obtener_usuario_por_id(id):
    try:
        user = Usuario.query.get(id)
        if user:
            return user.to_dict()
        else:
            return jsonify({"error": "Usuario no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def crear_usuario(name, email, password):
    try:
        nuevo_usuario = Usuario(name, email, password)
        db.session.add(nuevo_usuario)
        db.session.commit()
        return nuevo_usuario.to_dict()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)})

def editar_usuario(id, name, email):
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({"error": "El usuario no existe"})
    
    usuario.name = name
    usuario.email = email
    try:
        db.session.commit()
        return jsonify({"message": "Usuario modificado"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Error modificando el usuario: {str(e)}"})

def eliminar_usuario(id):
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({"error": "El usuario no existe"})
    try:
        db.session.delete(usuario)
        db.session.commit()
        return jsonify({"message": "Usuario eliminado"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Error eliminando el usuario: {str(e)}"})

def iniciar_sesion_usuario(email, password):
    usuario = Usuario.query.filter_by(email=email).first()
    if usuario and usuario.check_password(password):
        access_token = create_access_token(identity=usuario.id)
        return jsonify({
            'access_token': access_token,
            'usuario': {
                "id": usuario.id,
                "name": usuario.name,
                "email": usuario.email
            }
        })
    return jsonify({"msg": "Credenciales inválidas"}), 401