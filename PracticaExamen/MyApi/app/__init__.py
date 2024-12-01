import random

import string

from flask import Flask

from .director.routes import directoresBP

from .supermercado.routes import supermercadosBP



from flask_jwt_extended import JWTManager

caracteres = string.ascii_letters + string.digits

password = ''.join(random.choice(caracteres) for i in range(8))

app = Flask(__name__)

app.config['SECRET_KEY'] = password

jwt = JWTManager(app)

app.register_blueprint(directoresBP, url_prefix = '/directores')

app.register_blueprint(supermercadosBP, url_prefix = '/supermercados')
