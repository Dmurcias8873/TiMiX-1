from app import db

class Generacion(db.Model):
    
    __tablename__ = 'Generaciones'

    idGeneracion = db.Column(db.Integer, primary_key=True. autoincrement = True)
    NombreG = db.Column(db.String, nullable=False)
    Canciones = db.relationship('Cancion', backref='generacion', uselist=True)