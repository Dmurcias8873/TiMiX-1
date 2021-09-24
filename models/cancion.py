
from app import db


class Cancion(db.Model):

    __tablename__ = 'Canciones'

    idcancion = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String, nullable=False)
    Año = db.Column(db.Integer, nullable=False)
    # ArtistaId = db.Column(db.integer, nullable=False)
    # AlbumId = db.Column(db.integer, nullable=False)
    # CategoryId = db.Column(db.integer, nullable=False)
    # GeneracionId = db.Column(db.integer, nullable=False)

    @staticmethod
    def get_all():
        return Cancion.query.all()

    @staticmethod
    def get_id():
        return Cancion.query.filter_by(idcancion = 2).first()
    
    @staticmethod
    def get_cancion(nombre):
        return Cancion.query.filter_by(Nombre=nombre).first()
    
  
