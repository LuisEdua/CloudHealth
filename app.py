from flask import Flask
from flask_cors import CORS
#from CloudHealt.Infrestructure.Routes import 
from src.CloudHealt.Infrestructure.Routes import UsuariosRoute, HabitacionesRoute, AreasRoute, DeportesRoute, DiagnosticoRoute, FloorRoute, QuirofanoRoute, RolesRoute, TratamientosRoute

print("Ejecutando API")

def create_app():
    app = Flask(__name__);
    app.register_blueprint(UsuariosRoute.DataRoutes, url_prefix='/api');
    app.register_blueprint(HabitacionesRoute.DataRoutes, url_prefix='/api');
    app.register_blueprint(AreasRoute.DataRoutes, url_prefix='/api');
    app.register_blueprint(FloorRoute.DataRoutes, url_prefix='/api');
    app.register_blueprint(QuirofanoRoute.DataRoutes, url_prefix='/api');
    app.register_blueprint(DiagnosticoRoute.DataRoutes, url_prefix='/api');
    app.register_blueprint(DeportesRoute.DataRoutes, url_prefix='/api');
    app.register_blueprint(RolesRoute.DataRoutes, url_prefix='/api');
    app.register_blueprint(TratamientosRoute.DataRoutes, url_prefix='/api');


    CORS(app)
    return app

app = create_app();


if __name__ == '__main__':    
    print("API ejecutada Correctamente")    
    app.run(debug=True)