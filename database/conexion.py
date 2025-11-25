import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",        # En XAMPP normalmente está vacío
        database="mi_base"
    )

    return conexion
    
except mysql.connector.Error as error:
        print("error al conectar a la base de datos", error)
        return none