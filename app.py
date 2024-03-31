from flask import Flask
from flask_cors import CORS
from src.CloudHealt.Infrestructure.Routes import UsersRoute, HabitacionesRoute

print("Ejecutando API")

def create_app():
    app = Flask(__name__);
    app.register_blueprint(UsersRoute.DataRoutes, url_prefix='/api');
    app.register_blueprint(HabitacionesRoute.DataRoutes, url_prefix='/api');
    CORS(app)
    return app

app = create_app();


if __name__ == '__main__':    
    print("API ejecutada Correctamente")    
    app.run(debug=True)