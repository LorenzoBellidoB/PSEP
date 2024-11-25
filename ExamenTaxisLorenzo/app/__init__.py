import random
import string
from flask import Flask
from .taxis.routes import taxisBP
from .reservas.routes import reservasBP
from .users.routes import usersBP
from flask_jwt_extended import JWTManager

caracteres = string.ascii_letters + string.digits
password = ''.join(random.choice(caracteres) for _ in range(8))

app = Flask(__name__)
app.config['SECRET_KEY'] = password
jwt = JWTManager(app)

app.register_blueprint(taxisBP, url_prefix='/taxis')
app.register_blueprint(reservasBP, url_prefix='/reservas')
app.register_blueprint(usersBP, url_prefix='/users')