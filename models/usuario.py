
from datetime import datetime
from app import db


class Usuario(db.Model):

    __tablename__ = 'Usuarios'

    idUsuario = db.Column(db.Integer, primary_key=True)
    NombreU = db.Column(db.String, nullable=False)
    Email = db.Column(db.String, nullable=False)
    RolId = db.Column(db.Integer, db.ForeignKey('roles.idRol'), nullable=False)
    Fecha = db.Column(db.Date, default = datetime.now, nullable=False)
    
    lista = db.relationship('Listas', backref='playlist', uselist = True)
    
        
    def __init__(self, NombreU, Email, RolId, Fecha):
        self.NombreU = NombreU
        self.Email = Email
        self.RolId = RolId
        self.Fecha = Fecha
        
    def __str__(self):
        return f'<Usuario> {self.idUsuario} {self.NombreU} {self.Email} {self.RolId} {self.Fecha}'
    
    @staticmethod
    def get_all():
        return Usuario.query.all()
    
    def create(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def get_email(email):
        return Usuario.query.filter_by(Email=email).first()
        
    @staticmethod
    def login():
        username = 'cliente'
        password = 'abc12345'