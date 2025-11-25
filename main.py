from modulos.estudiantes import agregar_estudiante, listar_estudiantes, buscar_estudiante

def menu ():

    while True:
        print("=== GESTOR DE ESTUDIANTES ===")
        print("1. Agragar estudiante")
        print("2.Listar estudiante")
        print("3.Buscar estudiante")
        print("4. Salir")

        opcion = input("selecciona una opcion")

        if opcion == "1":
            agregar_estudiante()
        elif opcion = "2":
            listar_estudiantes()
        elif opcion = "3":
            buscar_estudiante()
        elif opcion = "4":
            print("Saliendo del programa....")
            break
        else: print("opcion invalida \n")

if __name__"__main__":
    menu()

    




