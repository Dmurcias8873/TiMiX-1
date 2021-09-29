from app import db

class Generacion(db.Model):
    
    __tablename__ = 'Generaciones'

    idGeneracion = db.Column(db.Integer, primary_key=True. autoincrement = True)
    NombreG = db.Column(db.String, nullable=False)
    Canciones = db.relationship('Cancion', backref='generacion', uselist=True)
    
    def __init__(self, idGeneracion, NombreG):
        self.idGeneracion = idGeneracion
        self.NombreG = NombreG

    def __str__(self):
        return f'Album {self.idGeneracion} {self.NombreG}'

    @staticmethod
    def ListaGeneracion():
        return Generacion.query.all()