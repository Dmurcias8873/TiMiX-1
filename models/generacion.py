from app import db

class Generacion(db.Model):
    
    __tablename__ = 'Generaciones'

    idGeneracion = db.Column(db.Integer, primary_key=True, autoincrement = True)
    NombreG = db.Column(db.String, nullable=False)
    Canciones = db.relationship('Cancion', backref='generacion', uselist=True)
    
    def __init__(self, NombreG):
        self.NombreG = NombreG

    def __str__(self):
        return f'Generacion {self.idGeneracion} {self.NombreG}'

    def create(self):
        db.session.add(self)
        db.session.commit() 

    @staticmethod
    def ListaGeneracion():
        return Generacion.query.all()
    
    @staticmethod
    def get_id(Nombre):
        gen = Generacion.query.with_entities(Generacion.idGeneracion, Generacion.NombreG).filter_by(NombreG=Nombre).first()
        validate = bool(gen)
        if validate:
            return gen      
        else:
            createGeneracion = Generacion(Nombre)
            createGeneracion.create()
            gen = Generacion.query.with_entities(Generacion.idGeneracion, Generacion.NombreG).filter_by(NombreG=Nombre).first()
            return gen
