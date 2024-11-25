from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from app.utils.functions import EscribeFichero, Existe, FechaCorrecta, LeeFichero, NuevoId


taxisBP = Blueprint('taxis', __name__)
rutaTaxis = "app/ficheros/taxis.json"
rutaReservas = "app/ficheros/reservas.json"

@taxisBP.get("/")
def GetAllTaxis():
    taxis = LeeFichero(rutaTaxis)
    return jsonify(taxis)

@taxisBP.post("/reserva/<int:taxi_id>")
@jwt_required()
def Reservar(taxi_id):
    if request.is_json:

        taxis = LeeFichero(rutaTaxis)

        reservas = LeeFichero(rutaReservas)

        res = Existe(taxis, taxi_id)

        if res:
            nueva_reserva = request.get_json()
            for reserva in reservas:
                reserva["taxi_id"] = taxi_id
                
                for element in nueva_reserva:
                    reserva[element] = nueva_reserva[element]
                    
                if FechaCorrecta(nueva_reserva["fecha"]):
                    reserva["id"] == NuevoId(reservas)
                    reservas.append(reserva)
                    EscribeFichero(rutaReservas, reservas)
                    for taxi in taxis:
                        taxi["estado"] = reserva["usuario"]
                        taxi["ultima_reserva"] = reserva["fecha"]
                    return reserva, 200
                else:
                    return {"error": "Fecha incorrecta"}
                
        else:
            return {"error": "El taxi no existe o esta completo"}
                         
    else:
        return {"error": "Request must be JSON"}, 415


