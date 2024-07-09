from flask import Flask,render_template, request, redirect
from datauser import * # Importamos la base de datos Json
from controller_db import * # Importamos la base de datos MySQL


app = Flask(__name__)

@app.route('/index')
def dataindex():
    title = "Cartelera"
    return render_template('index.html', title=title)

@app.route('/contacto')
def datacontacto():
    title = "Contacto"
    return render_template('contacto.html', title=title)

@app.route('/persona')
def datapersona():
    usuarios = obtener_usuarios()
    title = "Persona"
    return render_template('persona.html', title=title, usuarios=usuarios)

@app.route('/criticas')
def datacriticas():
    title = "Criticas"
    return render_template('criticas.html', title=title)

@app.route('/estrenos')
def dataestrenos():
    title = "Estrenos"
    return render_template('estrenos.html', title=title)

@app.route('/quienes-somos')
def dataquienesSomos():
    title="Quienes Somos"
    return render_template('quienes-somos.html',title=title)

@app.route('/comunidad')
def dataComunidad():
    usuarios = obtener_usuarios()
    title = "Comunidad"    
    return render_template('comunidad.html', title=title, usuarios=usuarios)


