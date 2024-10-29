import random
import string
from flask import Flask
from .directores.routes import directoresBP
from .pelicula.routes import peliculasBP
from .users.routes import usersBP
from flask_jwt_extended import JWTManager

caracteres = string.ascii_letters + string.digits
password = ''.join(random.choice(caracteres) for _ in range(8))

app = Flask(__name__)
app.config['SECRET_KEY'] = password
jwt = JWTManager(app)

app.register_blueprint(directoresBP, url_prefix='/directores')
app.register_blueprint(peliculasBP, url_prefix='/peliculas')
app.register_blueprint(usersBP, url_prefix='/users')

