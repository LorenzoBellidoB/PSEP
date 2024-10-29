from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.utils.functions import *

peliculasBP = Blueprint('peliculas', __name__)
rutaPeliculas = "Cine/cineAnidado/app/ficheros/peliculas.json"
rutaDirectores = "Cine/cineAnidado/app/ficheros/directores.json"


@peliculasBP.get("/")
def get_PeliculasAll():
    peliculas = leeFichero(rutaPeliculas)
    return jsonify(peliculas)

@peliculasBP.get("/<int:id>")
def get_peliculas(id):
    peliculas = leeFichero(rutaPeliculas)
    for pelicula in peliculas:
        if pelicula['id'] == id:
            return pelicula, 200
    
    return{"error": "Director no encontrado"}, 404

@peliculasBP.post("/")
@jwt_required()
def add_pelicula():
    peliculas = leeFichero(rutaPeliculas)
    if request.is_json:
        pelicula = request.get_json()
        pelicula["id"] = nuevo_id(peliculas)
        peliculas.append(pelicula)
        escribeFichero(rutaPeliculas, peliculas)

        return pelicula, 201
    return{"error": "Request must be JSON"}, 415

@peliculasBP.put("/<int:id>")
@peliculasBP.patch("/<int:id>")
@jwt_required()
def modifyPelicula(id):
    peliculas = leeFichero(rutaPeliculas)
    if request.is_json:
        newPelicula = request.get_json()
        for pelicula in peliculas:
            if pelicula["id"] == id:
                for element in newPelicula:
                    pelicula[element] = newPelicula[element]
                peliculas.append(pelicula)
                escribeFichero(rutaPeliculas, peliculas)
                return pelicula, 200
    
    return {"error": "Request must be JSON"}, 415

@peliculasBP.delete("/<int:id>")
@jwt_required()
def deletePelicula(id):
    peliculas = leeFichero(rutaPeliculas)
    for pelicula in peliculas:
        if pelicula["id"] == id:
            peliculas.remove(pelicula)
            escribeFichero(rutaPeliculas, peliculas)
            return {}, 200
    return {"error":"No se ha podido borrar"}, 404