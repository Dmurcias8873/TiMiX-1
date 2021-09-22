
from app import database


class Cancion(database.Model):

    __tablename__ = 'Canciones'

    id_cancion = database.Column(database.Integer, primary_key=True)
    Nombre = database.Column(database.String, nullable=True)
    Año = database.Column(database.date, nullable=True)
    ArtistaId = database.Column(database.integer, nullable=True)
    AlbumId = database.Column(database.integer, nullable=True)
    CategoryId = database.Column(database.integer, nullable=True)
    GeneracionId = database.Column(database.integer, nullable=True)

    @staticmethod
    def get_all():
        return Cancion.query.all()
