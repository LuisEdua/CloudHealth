from flask import Flask
from src.CloudHealt.Infrestructure.Routes.PacientesRoutes import pacientes_routes
from flask_cors import CORS

app = Flask(__name__)

app.register_blueprint(pacientes_routes, url_prefix='/pacientes')

if __name__ == '__main__':
    app.run()
