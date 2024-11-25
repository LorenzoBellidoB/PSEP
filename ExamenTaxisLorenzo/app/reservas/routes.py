from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.utils.functions import EscribeFichero, LeeFichero

reservasBP = Blueprint('reservas', __name__)
rutaTaxis = "app/ficheros/reservas.json"
rutaReservas = "app/ficheros/reservas.json"

@reservasBP.get("/")
@jwt_required()
def GetAllReservas():
    reservas = LeeFichero(rutaReservas)
    return jsonify(reservas)

@reservasBP.delete("/<int:taxi_id>")

def deleteReserva(taxi_id):
    reservas = LeeFichero(rutaReservas)

    taxis = LeeFichero(rutaTaxis)
    for reserva in reservas:
        if reserva["taxi_id"] == taxi_id:

            for taxi in taxis:
                taxi["estado"] = "null"
                taxi["ultima_reserva"] = "null"
            taxis.append(taxi)
            EscribeFichero(rutaTaxis,taxis)

            reservas.remove(reserva)
            EscribeFichero(rutaReservas, reserva)
            return {}, 200
    return {"error":"No se ha podido borrar"}, 404