import pymysql

host = "marviotti.mysql.pythonanywhere-services.com"
user = "marviotti"
clave= "Thanks2024!"
db="marviotti$datauser-py"

def conexionMySQL():
    return pymysql.connect(host=host,user=user,password=clave,database=db)