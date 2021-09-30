
from app import db

class Rol(db.Model):
    __tablename__ = 'roles'

    idRol = db.Column(db.Integer, primary_key=True)
    NombreR = db.Column(db.String, nullable=False)
    
    usuarios = db.relationship('Usuario', backref='usuario', uselist = True)


