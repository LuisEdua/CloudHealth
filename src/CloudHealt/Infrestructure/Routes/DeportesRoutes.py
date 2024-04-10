from flask import request, Blueprint
from src.CloudHealt.Infrestructure.Repository.MySQLDeportesRepository import MySQLDeportesRepository
from src.CloudHealt.Infrestructure.Controllers.DeportesController.Get import GetController
from src.CloudHealt.Infrestructure.Controllers.DeportesController.Create import CreateController

repo = MySQLDeportesRepository()
get_controller = GetController(repo)
create_controller = CreateController(repo)

deportes_routes = Blueprint('deportes_routes', __name__)

@deportes_routes.route('/<string:historia_uuid>', methods=['GET'])
def Get(historia_uuid):
    return get_controller.run(historia_uuid)


@deportes_routes.route('/', methods=['POST'])
def Create():
    return create_controller.run(request)
