from models.producto import Producto
from config import db
from flask import jsonify

def obtener_todos_los_productos():
    try:
        return [product.to_dict() for product in Producto.query.all()]
    except Exception as e:
        return jsonify({"error": str(e)})

def obtener_producto_por_id(id):
    try:
        product = Producto.query.get(id)
        if product:
            return product.to_dict()
        else:
            return jsonify({"error": "Producto no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def crear_producto(nombre, marca, precio, stock):
    try:
        nuevo_producto = Producto(nombre, marca, precio, stock)
        db.session.add(nuevo_producto)
        db.session.commit()
        return nuevo_producto.to_dict()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)})

def editar_producto(id, nombre, marca, precio, stock):
    producto = Producto.query.get(id)
    if not producto:
        return jsonify({"error": "El producto no existe"})
    
    producto.nombre = nombre
    producto.marca = marca
    producto.precio = precio
    producto.stock = stock
    try:
        db.session.commit()
        return jsonify({"message": "Producto modificado"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Error modificando el producto: {str(e)}"})

def eliminar_producto(id):
    producto = Producto.query.get(id)
    if not producto:
        return jsonify({"error": "El producto no existe"})
    try:
        db.session.delete(producto)
        db.session.commit()
        return jsonify({"message": "Producto eliminado"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Error eliminando el producto: {str(e)}"})