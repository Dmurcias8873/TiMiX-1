from app import db

class Artista(db.Model):  
    __tablename__ = 'Artistas'

    idArtista = db.Column(db.Integer, primary_key=True, autoincrement = True)
    NombreA = db.Column(db.String, nullable=False)
    Nacionalidad = db.Column(db.String, nullable=False)

    def __init__(self, idArtista, Nombre, Nacionalidad):
        self.idArtista = idArtista
        self.NombreA = Nombre
        self.Nacionalidad = Nacionalidad 
    
    def __str__(self):
        return f'Artista {self.idArtista} {self.NombreA} {self.Nacionalidad}'

    @staticmethod
    def ListarArtista():
        return Artista.query.all()