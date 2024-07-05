import  pymysql

host = "localhost"
user = "root"
password = "clave"
database = "db"

def conexionMySQL():
    return pymysql.connect(host="localhost", user="root", password="clave", database="db")