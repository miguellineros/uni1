import mysql.connector
from mysql.connector import errorcode
from auxiliares.data_conexion import servidor,puerto,usuario,contrasena,base_datos

def generar_conexion():
    try:
        conexion = mysql.connector.connect(
            host=servidor,
            port=puerto,
            user=usuario,
            password=contrasena,
            database=base_datos
            )
        if conexion and conexion.is_connected():
            return conexion

    except mysql.connector.Error:
        print("error de conexion")


def leer_datos(consulta):
    conexion = generar_conexion()
    if conexion and conexion.is_connected():  
        cursor = conexion.cursor()
        cursor.execute(consulta)
        resultados = cursor.fetchall()
        print(resultados)
    else:
        print("erros de conexion")    
