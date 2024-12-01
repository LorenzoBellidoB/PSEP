from flask import Blueprint, jsonify, request

from flask_jwt_extended import jwt_required


from MyApi.app.utils.functions import LeerFichero

directoresBP = Blueprint('directores', __name__)


rutaDirectores = 'app/ficheros/directores.json'
rutaSupermercados = 'app/ficheros/directores.json'

@directoresBP.get("/")
def GetDirectoresAll():
    directores = LeerFichero(rutaDirectores)
    return jsonify(directores)

@directoresBP.get("/<int:id>")
def GetDirector(id):
    directores = LeerFichero(rutaDirectores)
    for director in directores:
        if director['id'] == id:
            return director, 200
    
    return{"error": "Director no encontrado"}, 404


@directoresBP.get("/<int:id>/supermercados")
def GetSupermercadosDirector(id):
    supermercados = LeerFichero(rutaSupermercados)
    list = []
    for supermercado in supermercados:
        if supermercado['idDirector'] == id:
            list.append(supermercado)

    if len(list) > 0:
        return list, 200
    else:
        return {"error": "Director no encontrado"}, 404