from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.utils.functions import *

directoresBP = Blueprint('directores', __name__)
rutaDirectores = "Cine/cineAnidado/app/ficheros/directores.json"
rutaPeliculas = "Cine/cineAnidado/app/ficheros/peliculas.json"

@directoresBP.get("/")
def get_directoresAll():
    directores = leeFichero(rutaDirectores)
    return jsonify(directores)

@directoresBP.get("/<int:id>")
def get_director(id):
    directores = leeFichero(rutaDirectores)
    for director in directores:
        if director['id'] == id:
            return director, 200
    
    return{"error": "Director no encontrado"}, 404

@directoresBP.get("/<int:id>/peliculas")
def get_peliculasDirector(id):
    peliculas = leeFichero(rutaPeliculas)
    list = []
    for pelicula in peliculas:
        if pelicula['idDirector'] == id:
            list.append(pelicula)
    
    if len(list) > 0:
        return list, 200
    else:
        return{"error": "Director no encontrado"}, 404
    
@directoresBP.post("/")
@jwt_required()
def add_director():
    directores = leeFichero(rutaDirectores)
    if request.is_json:
        director = request.get_json()

        director["id"] = nuevo_id(directores)

        directores.append(director)

        return director, 201
    return{"error": "Request must be JSON"}, 415

@directoresBP.put("/<int:id>")
@directoresBP.patch("/<int:id>")
@jwt_required()
def modifyDirector(id):
    directores = leeFichero(rutaDirectores)
    if request.is_json:
        newDirector = request.get_json()
        for director in directores:
            if director["id"] == id:
                for element in newDirector:
                    director[element] = newDirector[element]
                directores.append(director)
                escribeFichero(rutaDirectores, directores)
                
                return director, 200
    
    return {"error": "Request must be JSON"}, 415

@directoresBP.delete("/<int:id>")
@jwt_required()
def deleteDirector(id):
    directores = leeFichero(rutaDirectores)
    for director in directores:
        if director["id"] == id:
            directores.remove(director)
            escribeFichero(rutaDirectores, directores)
            return {}, 200
    return {"error":"No se ha podido borrar"}, 404