from app import db

class Artista(db.Model):  
    __tablename__ = 'Artistas'

    idArtista = db.Column(db.Integer, primary_key=True, autoincrement = True)
    NombreA = db.Column(db.String, nullable=False)
    Nacionalidad = db.Column(db.String, nullable= True)


    def __init__(self, NombreA):
        self.NombreA = NombreA
    
    def __str__(self):
        return f'Artista {self.idArtista} {self.NombreA} {self.Nacionalidad}'

    def create(self):
        db.session.add(self)
        db.session.commit() 
        
    @staticmethod
    def ListarArtista():
        return Artista.query.all()
    
    @staticmethod
    def get_id(Nombre):
        art = Artista.query.with_entities(Artista.idArtista, Artista.NombreA).filter_by(NombreA=Nombre).first()
        validate = bool(art)
        if validate:
            return art      
        else:
            createArtista = Artista(Nombre)
            createArtista.create()
            art = Artista.query.with_entities(Artista.idArtista, Artista.NombreA).filter_by(NombreA=Nombre).first() 
            return art