from flask import Blueprint, jsonify, request
from controllers.controllerUsuario import (
    obtener_todos_los_usuarios,
    obtener_usuario_por_id,
    crear_usuario,
    editar_usuario,
    eliminar_usuario,
    iniciar_sesion_usuario
)

user_bp = Blueprint('usuarios', __name__)

@user_bp.route('/', methods=['GET'])
def index():
    usuarios = obtener_todos_los_usuarios()
    return jsonify(usuarios)

@user_bp.route('/<id>', methods=['GET'])
def obtener_usuario(id):
    return obtener_usuario_por_id(id)

@user_bp.route('/crear', methods=['POST'])
def crear():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    nuevo_usuario = crear_usuario(name, email, password)
    return jsonify(nuevo_usuario)

@user_bp.route('/editar/<id>', methods=['POST'])
def editar(id):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    return editar_usuario(id, name, email)

@user_bp.route('/eliminar/<id>', methods=['DELETE'])
def eliminar(id):
    return eliminar_usuario(id)

@user_bp.route('/iniciar-sesion', methods=['POST'])
def iniciar_sesion():
    data = request.get_json()
    return iniciar_sesion_usuario(data['email'], data['password'])