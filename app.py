import re
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://glbybbbgetizbw:4a6d84cd18afa55a53ede162d298b2c6139a0987c0d432558dd91f1d5d5caec6@ec2-44-198-223-154.compute-1.amazonaws.com:5432/d6k8pf744iivoh'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bycrypt = Bcrypt(app)

from models.cancion import Cancion
from models.artista import Artista
from models.categoria import Categoria
from models.album import Album
from models.generacion import Generacion
from models.listas import Listas
from models.usuario import Usuario
from models.rol import Rol

@app.route('/registro')
def registro():

   username = 'DaironM'
   password = 'misiontic2021'
   email = 'ingemec.dmurcia@gmail.com'
   rol = Rol.get_id(2)
   user = Usuario(username, password, email, rol.idRol)
   user.create()
   return 'Usuario creado'

@app.route('/login')
def login():   
   password = 'misiontic2021'
   email = 'ingemec.dmurcia@gmail.com'
   valida = Usuario.login(email, password)
   return str(valida)


@app.route('/canciones')
def Listarcancion():
    NCancion = {}
    canciones = Cancion.filtroCancion()
    for cancion in canciones:
        NCancion[canciones.index(cancion)] = cancion.Nombre + ' ' + cancion.Duracion
        print (cancion)        
    return NCancion

@app.route('/fxcategoria')
def Listarcategoria():
    NCategoria = {}
    #categorias = Categoria.get_categorias(  )
    categorias = Cancion.filtroCategoria()
    for categoria in categorias:
        NCategoria[categorias.index(categoria)] = categoria.Nombre + ' ' + str(categoria.Año) + ' ' + categoria.Duracion
        print (categoria)      
    return NCategoria

@app.route('/fxartista')
def Listarartista():
    NArtista = {}
    artistas = Cancion.filtroArtista()
    for artista in artistas:
        NArtista[artistas.index(artista)] = artista.Nombre + ' ' + str(artista.Año) + ' ' + artista.Duracion
        print (artista)        
    return NArtista

@app.route('/fxgeneracion')
def Listargeneracion():
    NGeneracion = {}
    generaciones = Cancion.filtroGeneracion()
    for generacion in generaciones:
        NGeneracion[generaciones.index(generacion)] = generacion.__str__()
        print (generacion)        
    return NGeneracion

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