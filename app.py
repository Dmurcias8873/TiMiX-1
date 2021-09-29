from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://glbybbbgetizbw:4a6d84cd18afa55a53ede162d298b2c6139a0987c0d432558dd91f1d5d5caec6@ec2-44-198-223-154.compute-1.amazonaws.com:5432/d6k8pf744iivoh'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from models.cancion import Cancion
from models.usuario import Usuario
from models.rol import Rol

@app.route('/canciones')
def Listarcancion():
    NCancion = []
    canciones = Cancion.get_all()
    for cancion in canciones:
        NCancion.append(cancion.__str__())
        print (cancion)        
    return NCancion



#@app.route('/')
#def hello():
#    NCancion = ''
#    canciones = Cancion.get_all()
#    for cancion in canciones:
#        NCancion += cancion.Nombre
#        print(cancion)
#    return NCancion



#@app.rohte('/login')
#def login():
#def login():
#    success = False
#    user = Usuario.get_email(email)
#    
#    if (user):
#        