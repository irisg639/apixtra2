from config import db

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    marca = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    def _init_(self, nombre, marca, precio, stock):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.stock = stock

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "marca": self.marca,
            "precio": self.precio,
            "stock": self.stock
        }