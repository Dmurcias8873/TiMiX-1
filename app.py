
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


@app.route('/registro', methods = ['POST', 'GET'])
def registro():
    if request.method == 'POST':    
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        rol = Rol.get_id(2)
        user = Usuario(username, password, email, rol.idRol)
        user.create()
        flash('Usuario creado con exito')
        return redirect(url_for('index'))
    return render_template('registro.html')


@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':   
        password = request.form['password']
        email = request.form['email']
        valida = Usuario.login(email, password)
        if valida:
            user = Usuario.Nameuser(email)
            flash('Bienvenido' +' ' + str(user) +' ')
            return redirect(url_for('timix'))
        else:
            flash('Datos errados, verifique nuevamente')
            return redirect(url_for('index'))
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
    query = Cancion.query

    # search filter

    search = request.args.get('search[value]')
    if search:
        query = query.filter(db.or_(
            Cancion.Nombre.like(f'%{search}%'),
        ))
    total_filtered = query.count()


    # sorting
    order = []
    i = 0
    while True:
        col_index = request.args.get(f'order[{i}][column]')
        if col_index is None:
            break
        col_name = request.args.get(f'columns[{col_index}][data]')
        if col_name not in ['Nombre', 'Año', 'Duracion']:
            col_name = 'Nombre'
        descending = request.args.get(f'order[{i}][dir]') == 'desc'
        col = getattr(Cancion, col_name)
        if descending:
            col = col.desc()
        order.append(col)
        i += 1
    if order:
        query = query.order_by(*order)

    # pagination
    start = request.args.get('start', type=int)
    length = request.args.get('length', type=int)
    query = query.offset(start).limit(length)

    # response
    return {
        'data': [cancion.to_dict() for cancion in query],
        'recordsFiltered': total_filtered,
        'recordsTotal': Cancion.query.count(),
        'draw': request.args.get('draw', type=int),
    }


@app.route('/canciones')
def Listarcancion():
    NCancion = {}
    canciones = Cancion.get_all()
    for cancion in canciones:
        NCancion[canciones.index(cancion)] = cancion.Nombre + ' ' + str(cancion.Año) + ' ' + cancion.Duracion + ' ' + cancion.NombreCat + ' ' + cancion.NombreA + ' ' + cancion.Album + ' ' + cancion.NombreG
    return NCancion

@app.route('/fxcategoria')
def Listarcategoria():
    NCategoria = {}
    #categorias = Categoria.get_categorias(  )
    categorias = Cancion.filtroCategoria()
    for categoria in categorias:
        NCategoria[categorias.index(categoria)] = categoria.Nombre
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

if __name__ == '__main__':
    app.run(port = 3000)
