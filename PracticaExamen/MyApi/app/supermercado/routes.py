from flask import Blueprint, jsonify, request

from flask_jwt_extended import jwt_required

from app.utils.functions import *

supermercadosBP = Blueprint('supermecados', __name__)


rutaDirectores = 'MyApi/app/ficheros/directores'
rutaSupermercados = 'MyApi/app/ficheros/directores'