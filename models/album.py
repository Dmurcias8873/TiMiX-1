from re import A
from app import db


class Album(db.Model):  
    __tablename__ = 'Albumes'

    idAlbum = db.Column(db.Integer, primary_key=True, autoincrement = True)
    Album = db.Column(db.Integer, nullable=False)
    Caratula = db.Column(db.String, nullable= True)
    Canciones = db.relationship('Cancion', backref='album', uselist=True)


    def __init__(self, Album):
        self.Album = Album

    def __str__(self):
        return f'Album {self.idAlbum} {self.Album} {self.Caratula} {self.Canciones}'

    def create(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def ListarAlbum():
        return Album.query.all()

    @staticmethod
    def get_id(Nombre):
        alb = Album.query.with_entities(Album.idAlbum, Album.Album).filter_by(Album=Nombre).first()
        validate = bool(alb)
        if validate:
            return alb      
        else:
            createAlbum = Album(Nombre)
            createAlbum.create()
            alb = Album.query.with_entities(Album.idAlbum, Album.Album).filter_by(Album=Nombre).first()                       
            return alb
