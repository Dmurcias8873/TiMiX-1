from app import db


Userlist = db.Table('UserList', db.metadata,

    PlaylistId = db.Column(db.integer, db.ForeignKey('Playlist.idPlaylist'), nullable=False),
    CancionId = db.Column(db.integer, db.ForeignKey('Cancion.idCancion'), nullable=False)
)
