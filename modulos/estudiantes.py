from database.conexion import conector

def agregar_estudiante():

    nombre=input("ingrese nombre:")
    edad = int(input("engrese edad:"))
    correo = input("ingreso correo:")

    conexion = conector ()
    if conexion is None:
        return

    cursor = conexion.cursor()

    sql = "INSERT INTO estudiantes (nombre,edad, correo) VALUES (%s,%s,%s)"
    valores = (nombre, edad, correo)

    cursor.execute(sql, valores)

    conexion.commit()

    cursor.close()
    conexion.close()

    print("Estudiante agregado exitosamente.") # Mensaje de confirmación


def listar_estudiantes():

    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM estudiantes")
    resultados = cursor.fetchall()

    print("\n LISTADO DE ESTUDIANTES")
    print ("-" *40)
    for fila in resultados:
        print(f"ID: {fila[0]} | Nombre: {fila[1]} | Edad: {fila[2]} | Correo: {fila[3]}")

    print("-" * 40 + "\n")

    cursor.close()
    conexion.close()


def buscar_estudiante():
    id_buscar = input("ingrese el ID del estudiante")

    conexion = conectar()
    if conexion is None:
        return

    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM estudiantes WHERE id = %s", (id_buscar))
    resultados = cursor.fetchone()

    if resultado: 
        print ("\n ESTUDIANTES ENCONTRADOS")









