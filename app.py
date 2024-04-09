from flask import Flask
from src.CloudHealt.Infrestructure.Routes.CamasRoutes import camas_routes
from src.CloudHealt.Infrestructure.Routes.HistoriasRoutes import historias_routes
from src.CloudHealt.Infrestructure.Routes.PacientesRoutes import pacientes_routes
from src.CloudHealt.Infrestructure.Routes import UsuariosRoute, HabitacionesRoute, AreasRoute, DeportesRoute, DiagnosticoRoute, FloorRoute, QuirofanoRoute, RolesRoute, TratamientosRoute
from flask_cors import CORS

app = Flask(__name__)

app.register_blueprint(camas_routes, url_prefix='/camas')
app.register_blueprint(historias_routes, url_prefix="/historias")
app.register_blueprint(pacientes_routes, url_prefix="/pacientes")
app.register_blueprint(UsuariosRoute.DataRoutes, url_prefix='/usuarios')
app.register_blueprint(HabitacionesRoute.DataRoutes, url_prefix='/habitaciones')
app.register_blueprint(AreasRoute.DataRoutes, url_prefix='/areas')
app.register_blueprint(FloorRoute.DataRoutes, url_prefix='/floors')
app.register_blueprint(QuirofanoRoute.DataRoutes, url_prefix='/quirofano')
app.register_blueprint(DiagnosticoRoute.DataRoutes, url_prefix='/diagnostico')
app.register_blueprint(DeportesRoute.DataRoutes, url_prefix='/deportes')
app.register_blueprint(RolesRoute.DataRoutes, url_prefix='/roles')
app.register_blueprint(TratamientosRoute.DataRoutes, url_prefix='/tratamientos')
CORS(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
