from flask import request, Blueprint
from src.CloudHealt.Infrestructure.Repository.MySQLQuirofanoRepository import MySQLQuirofanoRepository
from src.CloudHealt.Infrestructure.Controllers.QuirofanosControllers.Create import CreateController
from src.CloudHealt.Infrestructure.Controllers.QuirofanosControllers.ListAll import ListAllController
from src.CloudHealt.Infrestructure.Controllers.QuirofanosControllers.ListByFloor import ListByFloorController

repo = MySQLQuirofanoRepository()
create_controller = CreateController(repo)
list_all_controller = ListAllController(repo)
list_by_floor_controller = ListByFloorController(repo)

DataRoutes = Blueprint("quirofano_routes", __name__)


@DataRoutes.route('/', methods=['POST'])
def quirofano_crear():
    return create_controller.run(request)


@DataRoutes.route('/', methods=['GET'])
def quirofanos_listar():
    return list_all_controller.run()


@DataRoutes.route('/<string:floor_uuid>', methods=['GET'])
def quirofanos_by_floor(floor_uuid):
    return list_by_floor_controller.run(floor_uuid)
