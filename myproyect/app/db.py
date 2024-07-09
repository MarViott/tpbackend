import pymysql

host = "localhost"
user = "root"
clave= ""
db="seronoser"


def conexionMySQL():
    return pymysql.connect(host=host,user=user,password=clave,database=db)