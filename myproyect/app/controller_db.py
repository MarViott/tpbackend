from db import conexionMySQL


# Read - select
def obtener_usuarios():
    # conexion
    conexion = conexionMySQL()
    # consulta db
    with conexion.cursor() as cursor:
        # Read 
        query = "SELECT * FROM usuarios ORDER BY id"
        cursor.execute(query)
               
    # procesar los resultados -> fetch
        result = cursor.fetchall()
        
    # cerrar la conexion
        conexion.commit()
        conexion.close()
        return result
    

def cargar_nuevo_usuario(nombre, email, ocupacion):
    conexion = conexionMySQL()
    with conexion.cursor() as cursor:
        query = "INSERT INTO usuarios (nombre, email, ocupacion) VALUES (%s, %s, %s)"
        cursor.execute(query, (nombre, email, ocupacion))
        result = cursor
        conexion.commit()
        conexion.close()
        return result
    

def obtener_usuario_por_id(id):
    conexion = conexionMySQL()
    with conexion.cursor() as cursor:
        query="SELECT * FROM usuarios WHERE id = %s"
        cursor.execute(query, (id))
        usuario = cursor.fetchone()
    conexion.commit()
    conexion.close()
    return usuario


def actualizar_usuario(nombre, email, ocupacion, id):
    conexion = conexionMySQL()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE usuarios SET nombre = %s, email = %s, ocupacion = %s WHERE id = %s",(nombre, email, ocupacion, id))
        result = cursor
    conexion.commit()
    conexion.close()
    return result

# borrar -> delete
def eliminar_usuario(id):
    conexion = conexionMySQL()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM usuarios WHERE id = %s", (id))
        result = cursor
    conexion.commit()
    conexion.close()
    return result