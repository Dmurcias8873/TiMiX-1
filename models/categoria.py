from app import db

class Categoria(db.Model):
    
    __tablename__ = 'Categorias'

    idCategoria = db.Column(db.Integer, primary_key=True, autoincrement = True)
    NombreCat = db.Column(db.String, nullable=False)
    Canciones = db.relationship('Cancion', backref='categoria', uselist=True)
    
    def __init__(self, NombreCat):
        self.NombreCat = NombreCat
    
    def __str__(self):
        return f'Categoria {self.idCategoria} {self.NombreCat}'
    
    def to_dict(self):
        return {
            'NombreCat': self.NombreCat
        }   

    def create(self):
        db.session.add(self)
        db.session.commit()     
    
    @staticmethod
    def Listarcategoria():
        return Categoria.query.all()
    
    @staticmethod
    def get_id(Nombre):
        cat = Categoria.query.with_entities(Categoria.idCategoria, Categoria.NombreCat).filter_by(NombreCat=Nombre).first()
        validate = bool(cat)
        if validate:
            return cat      
        else:
            createCategoria = Categoria(Nombre)
            createCategoria.create()
            cat = Categoria.query.with_entities(Categoria.idCategoria, Categoria.NombreCat).filter_by(NombreCat=Nombre).first() 
            return cat
