import requests

token = ""
username = input("User: ")
password = input("Password: ")
resultado = requests.post("http://localhost:5050/users/login",
json={"username": username, "password": password},
headers={"Content-Type": "application/json"})
if resultado:
    token = resultado.json().get("token")
    print(token)
    api = True
else:
    api = False
    print("Error")



if(api):
   print("API CINE")
   print("1. Director.")
   print("2. Pelicula.")
   print("0. Salir.")

   opc = int(input("Introduce una opc: "))
   while opc != 0:
      if opc == 1:
         print("DIRECTOR")
         print("1. Obtener Directores.")
         print("2. Obtener Director.")
         print("3. Crear Director.")
         print("4. Modificar Director.")
         print("5. Modificar Atributo Director.")
         print("6. Borrar Director.")
         print("0. Salir.")
         opc = int(input("Introduce una opc: "))
         if opc == 1:
                  try:
                     response = requests.get("http://localhost:5050/directores",headers={"Authorization": "Bearer " + token})
                  except Exception as e:
                     print(e)

                  # Si la petición es exitosa
                  if response.status_code == 200:
                  # Muestra el json correspondiente a la petición
                     print(response.json())
                  # Si no, muestra este mensaje
                  else:
                     print("Se ha producido un error")
                  opc = 0
                  
         elif opc == 2:
                  try:
                     id =input("Introduce el id del director: ")
                     response = requests.get("http://localhost:5050/directores/" + id,headers={"Authorization": "Bearer " + token})
                  except Exception as e:
                     print(e)

                  # Si la petición es exitosa
                  if response.status_code == 200:
                  # Muestra el json correspondiente a la petición
                     print(response.json())
                  # Si no, muestra este mensaje
                  else:
                     print("Se ha producido un error")
                  opc = 0

         elif opc == 3:
                  nombre = input("Introduzca el nombre: ")
                  apellidos = input("Introduzca los apellidos: ")
                  dni = input("Introduzca el dni: ")
                  nacionalidad = input("Introduzca la nacionalidad: ")
                  nuevoDirector = {"nombre":nombre,"apellidos":apellidos,"dni":dni,"nacionalidad":nacionalidad}

                  try:
                     response = requests.post("http://localhost:5050/directores/",json=nuevoDirector,headers={"Authorization": "Bearer " + token})
                  except Exception as e:
                     print(e)

                  # Si la petición es exitosa
                  if response.status_code == 200:
                  # Muestra el json correspondiente a la petición
                     print(response.json())
                  # Si no, muestra este mensaje
                  else:
                     print("Se ha producido un error")
                  opc = 0

         # elif opc == 4:
         #          id = input("Introduzca un id: ")
         #          print("1. Modificar DNI.")
         #          print("2. Modificar nombre.")
         #          print("3. Modificar apellidos.")
         #          print("4. Modificar nacionalidad.")
         #          opc = int(input("Introduce una opcion: "))
         #          if opc == 1:
         #                dni = input("Introduce el dni nuevo")
         #                elemento = {"dni":dni}
         #                print(patchDirector(id,elemento))
         #          elif opc == 2:
         #                nombre = input("Introduce el nombre nuevo")
         #                elemento = {"dni":nombre}
         #                print(patchDirector(id,elemento))
         #          elif opc == 3:
         #                apellido = input("Introduce el apellido nuevo")
         #                elemento = {"dni":apellido}
         #                print(patchDirector(id,elemento))
         #          elif opc == 4:
         #                nacionalidad = input("Introduce la nacionalidad nuevo")
         #                elemento = {"dni":nacionalidad}
         #                print(patchDirector(id,elemento))
         elif opc == 5:
                  try:
                     id =input("Introduce el id del director: ")
                     response = requests.delete("http://localhost:5050/directores/" + id,headers={"Authorization": "Bearer " + token})
                  except Exception as e:
                     print(e)

                  # Si la petición es exitosa
                  if response.status_code == 200:
                  # Muestra el json correspondiente a la petición
                     print(response.json())
                  # Si no, muestra este mensaje
                  else:
                     print("Se ha producido un error")

         elif opc == 6:
            try:
               id = input("Introduce el id del director: ")
               response = requests.delete("http://localhost:5050/directores/" + id,headers={"Authorization": "Bearer " + token})
            except Exception as e:
               print(e)

            # Si la petición es exitosa
            if response.status_code == 200:
            # Muestra el json correspondiente a la petición
               print(response.json())
            # Si no, muestra este mensaje
            else:
               print("Se ha producido un error")
            opc = 0
      
      if opc == 2:
         print("PELICULA")
         print("1. Obtener Peliculas.")
         print("2. Obtener Pelicula.")
         print("3. Crear Pelicula.")
         print("4. Modificar Pelicula.")
         print("5. Modificar Atributo Pelicula.")
         print("6. Borrar Pelicula.")
         print("0. Salir.")
         opc = int(input("Introduce una opc: "))
         if opc == 1:
                  try:
                     response = requests.get("http://localhost:5050/peliculas",headers={"Authorization": "Bearer " + token})
                  except Exception as e:
                     print(e)

                  # Si la petición es exitosa
                  if response.status_code == 200:
                  # Muestra el json correspondiente a la petición
                     print(response.json())
                  # Si no, muestra este mensaje
                  else:
                     print("Se ha producido un error")
                  opc = 0

                  
         elif opc == 2:
                  try:
                     id = input("Introduce el id de la pelicula: ")
                     response = requests.get("http://localhost:5050/peliculas/" + id,headers={"Authorization": "Bearer " + token})
                  except Exception as e:
                     print(e)

                  # Si la petición es exitosa
                  if response.status_code == 200:
                  # Muestra el json correspondiente a la petición
                     print(response.json())
                  # Si no, muestra este mensaje
                  else:
                     print("Se ha producido un error")
                  opc = 0

         elif opc == 3:
                  titulo = input("Introduce el titulo")
                  duracion = input("Introduce la duracion")
                  idDirector = input("Introduce el id del director")
                  nuevaPelicula = {"titulo": titulo,"duracion":duracion,"idDirector":idDirector}

                  try:
                      response = requests.post("http://localhost:5050/peliculas/",json=nuevaPelicula,headers={"Authorization": "Bearer" + token})
                  except Exception as e:
                      print(e)

                  if response.status_code == 201:
                      print(response.json())
                  else:
                      print("Se ha producido un error")
                  opc = 0

                  
         # elif opc == 4:
         #          id = input("Introduzca un id: ")
         #          print("1. Modificar titulo.")
         #          print("2. Modificar duracion.")
         #          print("3. Modificar director.")
         #          opc = int(input("Introduce una opcion: "))
         #          if opc == 1:
         #                titulo = input("Introduce el titulo nuevo")
         #                elemento = {"titulo":titulo}
         #                print(patchPelicula(id,elemento))
         #          elif opc == 2:
         #                duracion = input("Introduce la duracion nuevo")
         #                elemento = {"duracion":duracion}
         #                print(patchPelicula(id,elemento))
         #          elif opc == 3:
         #                director = input("Introduce el director nuevo")
         #                elemento = {"director":director}
         #                print(patchPelicula(id,elemento))
         elif opc == 5:
                  try:
                     id =input("Introduce el id de la pelicula: ")
                     response = requests.get("http://localhost:5050/peliculas/" + id,headers={"Authorization": "Bearer " + token})
                  except Exception as e:
                     print(e)

                  # Si la petición es exitosa
                  if response.status_code == 200:
                  # Muestra el json correspondiente a la petición
                     print(response.json())
                  # Si no, muestra este mensaje
                  else:
                     print("Se ha producido un error")
         elif opc == 6:
            try:
               id = input("Introduce el id de la pelicula: ")
               response = requests.delete("http://localhost:5050/peliculas/" + id,headers={"Authorization": "Bearer " + token})
            except Exception as e:
               print(e)

            # Si la petición es exitosa
            if response.status_code == 200:
            # Muestra el json correspondiente a la petición
               print(response.json())
            # Si no, muestra este mensaje
            else:
               print("Se ha producido un error")
            opc = 0
      
      
      print("API CINE")
      print("1. Director.")
      print("2. Pelicula.")
      print("0. Salir.")

      opc = int(input("Introduce una opc: "))