
from flask_bcrypt import check_password_hash
from app import db
from datetime import datetime
from app import bycrypt



class Usuario(db.Model):

    __tablename__ = 'Usuarios'

    idUsuario = db.Column(db.Integer, primary_key=True)
    NombreU = db.Column(db.String, nullable=False)
    Password = db.Column(db.String, nullable=False)
    Email = db.Column(db.String, nullable=False)
    rolId = db.Column(db.Integer, db.ForeignKey('roles.idRol'), nullable=False)
    Fecha = db.Column(db.Date, default = datetime.now, nullable=False)
    
    lista = db.relationship('Listas', backref='playlist', uselist = True)
    
        
    def __init__(self, NombreU, Password, Email, rolId):
        self.NombreU = NombreU
        self.Password = bycrypt.generate_password_hash(Password).decode('utf-8')
        self.Email = Email
        self.rolId = rolId
                
        
    def __str__(self):
        return f'<Usuario> {self.NombreU} {self.Email} {self.RolId} {self.Fecha}'
    
    @staticmethod
    def get_all():
        return Usuario.query.all()
    
    def create(self):
        db.session.add(self)
        db.session.commit()

        
    @staticmethod
    def login(email, password):
        success = False
        user = Usuario.query.filter_by(Email=email).first()
        if (user):        
            success = bycrypt.check_password_hash(user.Password, password)        
        return success