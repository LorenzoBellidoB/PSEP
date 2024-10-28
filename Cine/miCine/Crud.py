import string
from pip._vendor import requests

globalUrl = "http://127.0.0.1:5050"

def getDirector(num: str):
    url = globalUrl + "/" + num
    response = requests.get(url)
    res = response.json()
    return res

def getDirectores():
    response = requests.get(url)
    res = response.json()
    return res

def createDirector(dni:str, nombre:str, apellidos:str, nacionalidad:str):
    url = globalUrl + "/" + "directores"
    user = {"dni": dni, "nombre": nombre, "apellidos": apellidos, "nacionalidad": nacionalidad}
    response = requests.post(url,json=user)
    estado = response.status_code
    if estado == 200 | estado == 201:
        res = response.json()
    else:
        res = "No se ha podido crear. Status: " + str(estado)
    return res

def modDirector(id:str, dni:str, nombre:str, apellidos:str, nacionalidad:str):
    url = globalUrl + "/" + "directores/" + id
    user = {"dni": dni, "nombre": nombre, "apellidos": apellidos, "nacionalidad": nacionalidad}
    response = requests.put(url, json=user)
    estado = response.status_code
    if estado == 200:
        res = response.json()
    else:
        res = "No se ha modificado. Status: " + str(estado)
    return res

def patchDirector(id, modificado):
    url = globalUrl + "/" + "directores/" + id
    response = requests.patch(url, json=modificado)
    estado = response.status_code
    if estado == 200:
        res = response.json()
    else:
        res = "No se ha modificado. Status: " + str(estado)
    return res

def deleteDirector(id:str):
    url = globalUrl + "/" + "directores/" + id
    response = requests.delete(url)
    estado = response.status_code
    if estado == 200:
        res = "Borrado correctamente."
    else:
        res = "No se ha podido borrar. Status: " + str(estado)
    return res


def getPelicula(num: str):
    url = globalUrl + "/" + "peliculas/" + num
    response = requests.get(url)
    res = response.json()
    return res

def getPeliculas():
    url = ""
    response = requests.get(url)
    res = response.json()
    return res

def createPelicula(titulo:str, duracion:str, idDirector:str):
    url = globalUrl + "/" + "peliculas"
    user = {"titulo": titulo, "duracion": duracion, "idDirector": idDirector}
    response = requests.post(url,json=user)
    estado = response.status_code
    if estado == 200 | estado == 201:
        res = response.json()
    else:
        res = "No se ha podido crear. Status: " + str(estado)
    return res

def modPelicula(id:str, titulo:str, duracion:str, idDirector:str):
    url = globalUrl + "/" + "peliculas/" + id
    user = {"titulo": titulo, "duracion": duracion, "idDirector": idDirector}
    response = requests.put(url, json=user)
    estado = response.status_code
    if estado == 200:
        res = response.json()
    else:
        res = "No se ha modificado. Status: " + str(estado)
    return res

def patchPelicula(id, modificado):
    url = globalUrl + "/" + "peliculas/" + id
    response = requests.patch(url, json=modificado)
    estado = response.status_code
    if estado == 200:
        res = response.json()
    else:
        res = "No se ha modificado. Status: " + str(estado)
    return res

def deletePelicula(id:str):
    url = globalUrl + "/" + "peliculas/" + id
    response = requests.delete(url)
    estado = response.status_code
    if estado == 200:
        res = "Borrada correctamente."
    else:
        res = "No se ha podido borrar. Status: " + str(estado)
    return res
