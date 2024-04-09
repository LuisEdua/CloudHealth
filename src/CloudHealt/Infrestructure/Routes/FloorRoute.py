# Importaciones de librería (descargadas)
from flask import request, Blueprint
from src.Database.MySQL import session_local
from src.CloudHealt.Infrestructure.Controllers.PisosControllers.GetController import GetController
from src.CloudHealt.Infrestructure.Controllers.PisosControllers.CreateController import CreateController
from src.CloudHealt.Infrestructure.Repository.MySQLPisoRepository import MySQLPisoRepository

repo = MySQLPisoRepository()
get_controller = GetController(repo)
create_controller = CreateController(repo)


DataRoutes = Blueprint("pisos_routes", __name__)

#Crear Piso
@DataRoutes.route('/', methods=['POST'])
def pisoCrear():
    return create_controller.run(request)


@DataRoutes.route('/', methods=['GET'])
def pisoListar():        
    return get_controller.run()
