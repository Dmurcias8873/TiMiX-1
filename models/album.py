from app import db


class Album(db.Model):  
    __tablename__ = 'Albumes'

    idAlbum = db.Column(db.Integer, primary_key=True, autoincrement = True)
    Album = db.Column(db.Integer, nullable=False)
    Caratula = db.Column(db.String, nullable=False)
    Canciones = db.relationship('Cancion', backref='album', uselist=True)

    def __init__(self, Album, Caratula, Canciones):
        self.Album = Album
        self.Caratula = Caratula
        self.Canciones = Canciones
    
    def __str__(self):
        return f'Album {self.idAlbum} {self.Album} {self.Caratula} {self.Canciones}'

    @staticmethod
    def ListarAlbum():
        return Album.query.all()