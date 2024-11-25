import json

# Función que lee el fichero de la ruta especificada
def LeeFichero(ruta):
    archivo = open(ruta, "r")

    res = json.load(archivo)

    archivo.close()

    return res

# Función que escribe el fichero de la ruta especificada
def EscribeFichero(ruta, objeto):
    archivo = open(ruta, "w")

    json.dump(objeto, archivo)

    archivo.close()

# Función que establece un id nuevo progresivamente
def NuevoId(lista):
    return max(i ["id"] for i in lista ) +1

# Función que comprueba si un taxi existe y está libre
def Existe(lista, id):
    res = False
    for objeto in lista:
        if objeto["id"] == id:
            if objeto["estado"] == "null":
                res = True
    
    return res

# Funcion que comprueba si la fecha es correcta
def FechaCorrecta(fecha):
    res = True
    fechaSplit = fecha.split(" ")
    date = fechaSplit[0]
    hora = fechaSplit[1]
    return res