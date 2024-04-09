from flask import request, Blueprint
from src.CloudHealt.Infrestructure.Repository.MySQLAreaRepository import MySQLAreaRepository
from src.CloudHealt.Infrestructure.Controllers.AreasControllers.Create import CreateController
from src.CloudHealt.Infrestructure.Controllers.AreasControllers.ListAll import ListAllController
from src.CloudHealt.Infrestructure.Controllers.AreasControllers.ListByFloor import ListByFloorController
from src.CloudHealt.Infrestructure.Controllers.AreasControllers.FindById import FindByIdController

repo = MySQLAreaRepository()
create_controller = CreateController(repo)
list_all_controller = ListAllController(repo)
list_by_floor_controller = ListByFloorController(repo)
find_by_id_controller = FindByIdController(repo)

DataRoutes = Blueprint("areas_routes", __name__)


# Crear Area
@DataRoutes.route('/', methods=['POST'])
def area_crear():
    return create_controller.run(request)


# Listar areas
@DataRoutes.route('/', methods=['GET'])
def areas_listar():
    return list_all_controller.run()


# Obtener Habitacion por Id
@DataRoutes.route('/<string:uuid>', methods=['GET'])
def area_by_uuid(uuid):
    return find_by_id_controller.run(uuid)


# Obtener areas por pisos
@DataRoutes.route('/piso/<string:uuid>', methods=['GET'])
def find_by_floor(uuid):
    return list_by_floor_controller.run(uuid)
