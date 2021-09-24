
from app import db


class Usuario(db.Model):

    __tablename__ = 'Usuarios'

    idUsuario = db.Column(db.Integer, primary_key=True)
    NombreU = db.Column(db.String, nullable=False)
    Email = db.Column(db.String, nullable=False)
    RolId = db.Column(db.Integer, db.ForeignKey('roles.idRol'), nullable=False)
    Fecha = db.Column(db.date, nullable=False)
    
    
    def __init__(self, NombreU, Email, RolId, Fecha):
        self.NombreU = NombreU
        self.Email = Email
        self.RolId = RolId
        self.Fecha = Fecha
    
    @staticmethod
    def get_all():
        return Usuario.query.all()
    
    def create(self):
        db.session.add(self)
        db.session.commit()