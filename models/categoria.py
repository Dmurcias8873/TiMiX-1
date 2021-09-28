from app import db

class Categoria(db.Model):
    
    __tablename__ = 'Categorias'

    idCategoria = db.Column(db.Integer, primary_key=True. autoincrement = True)
    NombreCat = db.Column(db.String, nullable=False)
    Canciones = db.relationship('Cancion', backref='categoria', uselist=True)