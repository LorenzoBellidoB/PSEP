from flask import *
from flask_jwt_extended import JWTManager
app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave'
jwt = JWTManager(app)

directores = [
    {"id":1,"dni":"08368686R","nombre":"Lorenzo","nacionalidad":"Espanola"},
    {"id":2,"dni":"08368234R","nombre":"Marco","nacionalidad":"Espanola"}
]

peliculas = [
    {"id":1, "titulo":"El Lobo de WallStreet","duracion":"2 horas","idDirector": 2},
    {"id":2, "titulo":"Harry Potter 3","duracion":"2 horas","idDirector": 1}
]

def findNewDirectorId():
    return max(director["id"] for director in directores) +1

def findNewPeliculaId():
    return max(pelicula["id"] for pelicula in peliculas) +1

@app.route('/')
def index():
    return "Bienvenido a mi Cine"

@app.get("/directores")
def get_DirectoresAll():
    return jsonify(directores)

@app.get("/directores/<int:id>")
@app.get("/director/<int:id>")
def get_directores(id):
    for director in directores:
        if director['id'] == id:
            return director, 200
    
    return{"error": "Director no encontrado"}, 404

@app.get("/peliculas")
def get_PeliculasAll():
    return jsonify(peliculas)

@app.get("/peliculas/<int:id>")
@app.get("/pelicula/<int:id>")
def get_peliculas(id):
    for pelicula in peliculas:
        if pelicula['id'] == id:
            return pelicula, 200
    
    return{"error": "Director no encontrado"}, 404

@app.post("/directores")
def add_director():
    if request.is_json:
        director = request.get_json()

        director["id"] = findNewDirectorId()

        directores.append(director)

        return director, 201
    return{"error": "Request must be JSON"}, 415

@app.post("/peliculas")
def add_pelicula():
    if request.is_json:
        pelicula = request.get_json()
        pelicula["id"] = findNewPeliculaId()
        peliculas.append(pelicula)

        return pelicula, 201
    return{"error": "Request must be JSON"}, 415

@app.put("/directores/<int:id>")

@app.patch("/directores/<int:id>")
def modifyDirector(id):
    if request.is_json:
        newDirector = request.get_json()
        for director in directores:
            if director["id"] == id:
                for element in newDirector:
                    director[element] = newDirector[element]
                
                return director, 200
    
    return {"error": "Request must be JSON"}, 415

@app.put("/peliculas/<int:id>")
@app.patch("/peliculas/<int:id>")
def modifyPelicula(id):
    if request.is_json:
        newPelicula = request.get_json()
        for pelicula in peliculas:
            if pelicula["id"] == id:
                for element in newPelicula:
                    pelicula[element] = newPelicula[element]
                
                return pelicula, 200
    
    return {"error": "Request must be JSON"}, 415

@app.delete("/directores/<int:id>")
def deleteDirector(id):
    for director in directores:
        if director["id"] == id:
            directores.remove(director)
            return {}, 200
    return {"error":"No se ha podido borrar"}, 404

@app.delete("/peliculas/<int:id>")
def deletePelicula(id):
    for pelicula in peliculas:
        if pelicula["id"] == id:
            peliculas.remove(pelicula)
            return {}, 200
    return {"error":"No se ha podido borrar"}, 404

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 5050)