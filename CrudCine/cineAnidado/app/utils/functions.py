import json

def leeFichero(ruta):
    archivo=open(ruta, "r")
    res = json.load(archivo)
    archivo.close()
    return res

def escribeFichero(ruta, objeto):
    archivo = open(ruta, "w")
    json.dump(objeto, archivo)
    archivo.close()

def nuevo_id(lista):
    return max(i ["id"] for i in lista ) +1