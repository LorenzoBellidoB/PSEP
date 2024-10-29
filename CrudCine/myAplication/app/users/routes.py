import bcrypt
from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from app.utils.functions import *

usersBP = Blueprint('users', __name__)
rutaUsuarios = "Cine/myAplication/app/ficheros/users.json"



@usersBP.post('/')
def registerUser():
    users = leeFichero(rutaUsuarios)
    if request.is_json:
        
        user = request.get_json()

        password = user["password"].encode("utf-8")

        sal = bcrypt.gensalt()

        hashPassword = bcrypt.hashpw(password,sal).hex()

        user["password"] = hashPassword

        users.append(user)

        escribeFichero(rutaUsuarios, users)

        token = create_access_token(identity=user['username'])
        return {"token":token}, 201
    
    return {"error": "Error"}, 415


@usersBP.post("/login")
def getUsuario():
   if request.is_json:
       user = request.get_json()
       username = user["username"]
       password = user["password"]
       usuarios = leeFichero(rutaUsuarios)
       for usuario in usuarios:
           if usuario["username"] == username and bcrypt.checkpw(password.encode("utf-8"),bytes.fromhex(usuario["password"])):
               return {"token": create_access_token(identity=username)}, 200
       return {"token":""}, 401
   return {"error": "Request must be JSON"}, 415
    

@usersBP.get('/')
def loginUser():
    users = leeFichero(rutaUsuarios)

    if request.is_json:
        user = request.get_json

        username = user["username"]

        password = user["password"].encode('utf-8')

        for userFile in users:
            if userFile["username"] == username:
                passwordFile = userFile["password"]

                if bcrypt.checkpw(password, bytes.fromhex(passwordFile)):
                    token = create_access_token(identity=username)
                    return {"token": token}, 201
                return {"error": "No tienes permiso"}, 401
            return {"error": "No existe el usuario"}
    
    return {"error": "Error"}, 415
