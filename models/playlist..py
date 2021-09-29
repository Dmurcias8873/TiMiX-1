from app import db

class Playlist(db.Model):
    
    __tablename__ = 'Playlist'

    idPlaylist = db.Column(db.Integer, primary_key=True. autoincrement = True)
    NombreP = db.Column(db.String, nullable=False)
    usuarioId = db.Column(db.integer, db.ForeignKey('Usuario.idUsuario'), nullable=False)  
    Userlist = db.relationship('UserList', backref='playlist', uselist=True)
    
    def __init__(self, idPlaylist, NombreP, usuarioId, UserList):
        self.idPlaylist = idPlaylist
        self.NombreP = NombreP
        self.usuarioId = usuarioId
        self.UserList = UserList
            
    def __str__(self):
        return f'Playlist {self.idPlaylist} {self.NombreP} {self.usuarioId} {self.UserList}'

    @staticmethod
    def ListarPlaylist():
        return Playlist.query.all()