from app import db


UserList = db.Table('UserList',
    db.Column('PlaylistId', db.Integer, db.ForeignKey('Playlist.idPlaylist'), primary_key=True),
    db.Column('CancionId', db.Integer, db.ForeignKey('Canciones.idcancion'), primary_key=True)
)
