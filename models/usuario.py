from config import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(60), nullable=False)
    email=db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    
    def __init__(self, name, email, password):
        self.name=name,
        self.email=email,
        self.password=generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return{
            "id":self.id,
            "name":self.name,
            "email":self.email,
            "password": self.password
        }