from app import db

class Album(db.Model):  
    __tablename__ = 'Albumes'

    idAlbum = db.Column(db.Integer, primary_key=True. autoincrement = True)
    Album = db.Column(db.Integer, nullable=False)
    Caratula = db.Column(db.String, nullable=False)
    Canciones = db.relationship('Cancion', backref='album', uselist=True)
