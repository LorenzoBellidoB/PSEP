from app import app
from app.utils.functions import FechaCorrecta

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 5050)