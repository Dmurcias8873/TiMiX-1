from app import db

class UserList(db.Model):
    
    __tablename__ = 'UserList'

    PlaylistId = db.Column(db.integer, db.ForeignKey('Playlist.idPlaylist'), nullable=False)
    CancionId = db.Column(db.integer, db.ForeignKey('Cancion.idCancion'), nullable=False)