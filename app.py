
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required, login_user, logout_user
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://glbybbbgetizbw:4a6d84cd18afa55a53ede162d298b2c6139a0987c0d432558dd91f1d5d5caec6@ec2-44-198-223-154.compute-1.amazonaws.com:5432/d6k8pf744iivoh'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.secret_key = 'mysecretkey'
bycrypt = Bcrypt(app)

from models.cancion import Cancion
from models.artista import Artista
from models.categoria import Categoria
from models.album import Album
from models.generacion import Generacion
from models.listas import Listas
from models.usuario import Usuario
from models.rol import Rol

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ICancion', methods = ['GET', 'POST'])
def insertdata():
    artistas = Artista.ListarArtista()
    albumes = Album.ListarAlbum()
    categorias = Categoria.Listarcategoria()
    generaciones = Generacion.ListaGeneracion()  
    if request.method == 'POST':
        artista = request.form['artistas']
        album = request.form['albumes']
        categoria = request.form['categorias']        
        generacion = request.form['generaciones']        
        cancion = request.form['cancion']        
        año = request.form['año']        
        duracion = request.form['duracion']
        vArtista = Artista.get_id(artista)
        vAlbum = Album.get_id(album)
        vCategoria = Categoria.get_id(categoria)
        vGeneracion = Generacion.get_id(generacion)
        canciones = Cancion(cancion, año, vArtista.idArtista, vAlbum.idAlbum, vCategoria.idCategoria, vGeneracion.idGeneracion, duracion )
        canciones.create()
        flash('Cancion ingresada con exito')       
        return redirect(url_for('insertdata'))                  
    return render_template('cancion.html', artistas= artistas, albumes= albumes, categorias= categorias, generaciones= generaciones)


@app.route('/registro', methods = ['GET', 'POST'])
def registro():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        rol = Rol.get_id(1)
        valida = Usuario.Nameuser(email)
        if valida:
            flash('Usuario se encuentra registrado')
            return redirect(url_for('registro')) 
        else:
            user = Usuario(username, password, email, rol.idRol)
            user.create()
            flash('Usuario creado con exito')
            return redirect(url_for('registro'))           
    return render_template('registro.html')

@app.route('/registro2', methods = ['GET', 'POST'])
def registro2():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        rol = Rol.get_id(2)
        valida = Usuario.Nameuser(email)
        if valida:
            flash('Admin se encuentra registrado')
            return redirect(url_for('registro2')) 
        else:
            user = Usuario(username, password, email, rol.idRol)
            user.create()
            flash('Usuario creado con exito')
            return redirect(url_for('registro2'))
    return render_template('registro2.html')


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form['password']
        email = request.form['email']
        valida = Usuario.login(email, password)
        user = Usuario.Nameuser(email)
        if valida and user.rolId== 2:
            flash('Bienvenido' +' administrador ' + str(user.NombreU) +' ')
            return redirect(url_for('insertdata'))
        elif valida and user.rolId==1:
            flash('Bienvenido' +' ' + str(user.NombreU) +' ')
            return redirect(url_for('timix'))
        else:
            flash('Datos errados, verifique nuevamente')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route('/tcancion')
def timix():
    return render_template('table.html', title='Listado de canciones')

@app.route('/api/data')
def data():
    song = Cancion.get_all()
    all_cancion=[]
    for cancion in song:
        all_cancion.append(
        {
            'Nombre': cancion.Nombre,
            'Año': cancion.Año,
            'Duracion': cancion.Duracion,
            'Album': cancion.Album,
            'Artista': cancion.NombreA,
            'Genero': cancion.NombreCat,
            'Generacion': cancion.NombreG
        }
        )
    return {'data': all_cancion}


if __name__ == '__main__':
    app.run(debug=False)
