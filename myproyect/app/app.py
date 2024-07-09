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

# insert
# 1) cargar el form
@app.route("/comunidad/cargar_usuario")
def insertComunidad():
    title = "Nuevo Usuario"
    return render_template("form_nuevo_usuario.html", title=title)
# 2) enviar los datos del form, por POST

@app.route("/tienda/guardar_nuevo_usuario", methods = ['POST'] )
def newUser_Comunidad():
    # print(request.form['nombre'])
    nombre_user = request.form['nombre']
    email_user = request.form['email']
    ocupacion_user = request.form['ocupacion']
    cargar_nuevo_usuario(nombre_user, email_user, ocupacion_user)
    return redirect("/comunidad")
    
# update
@app.route("/comunidad/editar_usuario/<int:id>")
def editar_usuario(id):
    title = "Editar Usuario"
    users_por_id = obtener_usuario_por_id(id)
    # print(usuarios_por_id)
    return render_template("form_editar_usuario.html", title=title, usuario=users_por_id[0])

@app.route("/comunidad/update_usuario", methods=['POST'])
def update_usuario():
    id_edit = request.form['id']
    nombre_edit = request.form['nombre']
    email_edit = request.form['email']
    ocupacion_edit = request.form['ocupacion']
    resp = actualizar_usuario(nombre_edit,email_edit,ocupacion_edit,id_edit)
    return redirect("/comunidad")
    # return render_template("comunidad.html", resp=resp)

# delete
@app.route('/comunidad/borrar_usuario/<int:id>')
def delete_usuario(id):
    eliminar_usuario(id)
    return redirect("/comunidad")
    