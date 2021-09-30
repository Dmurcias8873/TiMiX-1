from app import db


class Listas(db.Model):
    
    __tablename__ = 'Playlist'
    

    idPlaylist = db.Column(db.Integer, primary_key=True, autoincrement = True)
    NombreP = db.Column(db.String, nullable=False)
    usuarioId = db.Column(db.Integer, db.ForeignKey('Usuarios.idUsuario'), nullable=False)
    
    def __init__(self, idPlaylist, NombreP, usuarioId):
        self.idPlaylist = idPlaylist
        self.NombreP = NombreP
        self.usuarioId = usuarioId
            
    def __str__(self):
        return f'Playlist {self.idPlaylist} {self.NombreP} {self.usuarioId}'

    @staticmethod
    def ListarPlaylist():
        return Playlist.query.all()