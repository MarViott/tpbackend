from flask import Flask,render_template
from datauser import * # Importamos la base de datos Json
from controller_db import * # Importamos la base de datos MySQL

app = Flask(__name__)

@app.route('/index')
def dataindex():
    title = "Cartelera"
    return render_template('index.html', Cartelera=title)

@app.route('/contacto')
def datacontacto():
    title = "Contacto"
    return render_template('contacto.html', Contacto=title)

@app.route('/quienes-somos')
def dataquienes():
    title = "Quienes Somos"
    return render_template('quienes-somos.html', QuienesSomos=title)

@app.route('/criticas')
def datacriticas():
    title = "Criticas"
    return render_template('criticas.html', Criticas=title)

@app.route('/estrenos')
def dataestrenos():
    title = "Estrenos"
    return render_template('estrenos.html', Estrenos=title)

@app.route("/persona/<int:id>")
def dataUsers(id):
    title="Usuarios"
    return render_template("persona.html", title=title,user=users[id])
