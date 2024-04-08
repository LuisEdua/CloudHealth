from flask import Flask
from src.CloudHealt.Infrestructure.Routes.CamasRoutes import camas_routes
from flask_cors import CORS

app = Flask(__name__)

app.register_blueprint(camas_routes, url_prefix='/camas')
CORS(app)

if __name__ == '__main__':
    app.run()
