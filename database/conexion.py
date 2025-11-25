##import mysql.connector

##try:
  ##  conexion = mysql.connector.connect(
    ##    host="localhost",
      ##  user="root",
        ##password="",        # En XAMPP normalmente está vacío
        ##database="mi_base"
    ##)

    #return conexion
    
##except mysql.connector.Error as error:
  ##      print("error al conectar a la base de datos", error)
    ##    return none

import mysql.connector

def conector(): # <-- ¡Se define la función!
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",         # En XAMPP normalmente está vacío
            database="mi_base"
        )
        
        # El 'return' debe estar dentro de la función y de la rama try
        return conexion
        
    except mysql.connector.Error as error:
        print("Error al conectar a la base de datos:", error)
        
        # 'None' debe ser con la primera letra en mayúscula
        return None