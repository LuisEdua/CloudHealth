from flask import request, Blueprint
from src.CloudHealt.Infrestructure.Repository.MySQLLesionesRepository import MySQLLesionesRepository
from src.CloudHealt.Infrestructure.Controllers.LesionesControllers.Create import CreateController
from src.CloudHealt.Infrestructure.Controllers.LesionesControllers.Get import GetController

repo = MySQLLesionesRepository()
create_controller = CreateController(repo)
get_controller = GetController(repo)

lesiones_routes = Blueprint('lesiones_routes', __name__)

@lesiones_routes.route('/<string:historia_uuid>', methods=['GET'])
def Get(historia_uuid):
    return get_controller.run(historia_uuid)


@lesiones_routes.route('/', methods=['POST'])
def Create():
    return create_controller.run(request)
