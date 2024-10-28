from Crud import *


print("API CINE")
print("1. Director.")
print("2. Pelicula.")
print("0. Salir.")

opc = int(input("Introduce una opc: "))
while opc != 0:
    if opc == 1:
        print("DIRECTOR")
        print("1. Obtener Director.")
        print("2. Crear Director.")
        print("3. Modificar Director.")
        print("4. Modificar Atributo Director.")
        print("5. Borrar Director.")
        print("0. Salir.")
        opc = int(input("Introduce una opc: "))
        if opc == 1:
                id = input("Introduce el id: ")
                print(getDirector(id))
                opc = 0
                
        elif opc == 2:
                print(createDirector("08368666R", "Lorenzo", "Bellido", "Espanola"))
                opc = 0

        elif opc == 3:
                id = input("Introduce el id: ")
                print(modDirector(id, "08368666A", "Raul", "Romera", "Espanola"))

        elif opc == 4:
                id = input("Introduzca un id: ")
                print("1. Modificar DNI.")
                print("2. Modificar nombre.")
                print("3. Modificar apellidos.")
                print("4. Modificar nacionalidad.")
                opc = int(input("Introduce una opcion: "))
                if opc == 1:
                       dni = input("Introduce el dni nuevo")
                       elemento = {"dni":dni}
                       print(patchDirector(id,elemento))
                elif opc == 2:
                       nombre = input("Introduce el nombre nuevo")
                       elemento = {"dni":nombre}
                       print(patchDirector(id,elemento))
                elif opc == 3:
                       apellido = input("Introduce el apellido nuevo")
                       elemento = {"dni":apellido}
                       print(patchDirector(id,elemento))
                elif opc == 4:
                       nacionalidad = input("Introduce la nacionalidad nuevo")
                       elemento = {"dni":nacionalidad}
                       print(patchDirector(id,elemento))
        elif opc == 5:
                id = input("Introduce el id: ")
                print(deleteDirector(id))
    
    if opc == 2:
        print("PELICULA")
        print("1. Obtener Pelicula.")
        print("2. Crear Pelicula.")
        print("3. Modificar Pelicula.")
        print("4. Modificar Atributo Pelicula.")
        print("5. Borrar Pelicula.")
        print("0. Salir.")
        opc = int(input("Introduce una opc: "))
        if opc == 1:
                print(getPelicula(input(str("Introduce el id"))))
                opc = 0
                
        elif opc == 2:
                print(createPelicula("El Titanic", "3 horas", "1"))
                opc = 0

        elif opc == 3:
                print(modPelicula("1", "El Fary", "1 hora", "1"))

        elif opc == 4:
                id = input("Introduzca un id: ")
                print("1. Modificar titulo.")
                print("2. Modificar duracion.")
                print("3. Modificar director.")
                opc = int(input("Introduce una opcion: "))
                if opc == 1:
                       titulo = input("Introduce el titulo nuevo")
                       elemento = {"titulo":titulo}
                       print(patchPelicula(id,elemento))
                elif opc == 2:
                       duracion = input("Introduce la duracion nuevo")
                       elemento = {"duracion":duracion}
                       print(patchPelicula(id,elemento))
                elif opc == 3:
                       director = input("Introduce el director nuevo")
                       elemento = {"director":director}
                       print(patchPelicula(id,elemento))
        elif opc == 5:
                id = input("Introduce el id: ")
                print(deletePelicula(id))
        
    
    
    print("API CINE")
    print("1. Director.")
    print("2. Pelicula.")
    print("0. Salir.")

    opc = int(input("Introduce una opc: "))



