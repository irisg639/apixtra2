from flask import Blueprint, jsonify, request
from controllers.controllerProducto import (
    obtener_todos_los_productos,
    obtener_producto_por_id,
    crear_producto,
    editar_producto,
    eliminar_producto
)

producto_bp = Blueprint('productos', __name__)

@producto_bp.route('/', methods=['GET'])
def index():
    productos = obtener_todos_los_productos()
    return jsonify(productos)

@producto_bp.route('/<id>', methods=['GET'])
def obtener_producto(id):
    return obtener_producto_por_id(id)

@producto_bp.route('/crear', methods=['POST'])
def crear():
    data = request.get_json()
    nombre = data.get('nombre')
    marca = data.get('marca')
    precio = data.get('precio')
    stock = data.get('stock')
    nuevo_producto = crear_producto(nombre, marca, precio, stock)
    return jsonify(nuevo_producto)

@producto_bp.route('/editar/<id>', methods=['POST'])
def editar(id):
    data = request.get_json()
    nombre = data.get('nombre')
    marca = data.get('marca')
    precio = data.get('precio')
    stock = data.get('stock')
    return editar_producto(id, nombre, marca, precio, stock)

@producto_bp.route('/eliminar/<id>', methods=['DELETE'])
def eliminar(id):
    return eliminar_producto(id)