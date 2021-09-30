from app import db

class Artista(db.Model):  
    __tablename__ = 'Artistas'

    idArtista = db.Column(db.Integer, primary_key=True, autoincrement = True)
    Nombre = db.Column(db.String, nullable=False)
    Nacionalidad = db.Column(db.String, nullable=False)

    def __init__(self, idArtista, Nombre, Nacionalidad):
        self.idArtista = idArtista
        self.Nombre = Nombre
        self.Nacionalidad = Nacionalidad 
    
    def __str__(self):
        return f'Album {self.idArtista} {self.Nombre} {self.Nacionalidad}'

    @staticmethod
    def ListarArtista():
        return Artista.query.all()