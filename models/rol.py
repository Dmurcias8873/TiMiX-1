
from app import db

class Rol(db.Model):
    __tablename__ = 'roles'

    idRol = db.Column(db.Integer, primary_key=True)
    NombreR = db.Column(db.String, nullable=False)
    
    usuarios = db.relationship('Usuario', backref='usuario', uselist = True)

    def __init__(self, idRol, NombreR):
        self.idRol = idRol
        self.NombreR = NombreR
    
    def __str__(self):
        return f'Rol {self.idRol} {self.NombreR}'
    
    @staticmethod
    def get_categorias():
        return Rol.query.all()
    
    @staticmethod
    def get_id(id):
        return Rol.query.filter_by(idRol = id).first()
