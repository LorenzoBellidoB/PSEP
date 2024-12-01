import json

def LeerFichero(ruta):
    archivo = open(ruta, 'r')

    res = json.load(archivo)

    archivo.close()

    return res



def EscribeFichero(ruta, objeto):
    archivo = open(ruta, 'w')

    json.dump(objeto, archivo)

    archivo.close()


def NuevoId(lista):
    return max(i ["id"] for i in lista) + 1 