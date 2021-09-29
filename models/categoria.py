from app import db

class Categoria(db.Model):
    
    __tablename__ = 'Categorias'

    idCategoria = db.Column(db.Integer, primary_key=True. autoincrement = True)
    NombreCat = db.Column(db.String, nullable=False)
    Canciones = db.relationship('Cancion', backref='categoria', uselist=True)
    
def __init__(self, idCategoria, NombreCat):
    self.idCategoria = idCategoria
    self.NombreCat = NombreCat

def __str__(self):
    return f'Album {self.idCategoria} {self.NombreCat}'

@staticmethod
def ListarCategoria():
    return Categoria.query.all()