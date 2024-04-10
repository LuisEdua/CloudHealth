from flask import request, Blueprint
from src.CloudHealt.Infrestructure.Repository.MySQLRolRepository import MySQLRolRepository
from src.CloudHealt.Infrestructure.Controllers.RolesControllers.Get import GetController
from src.CloudHealt.Infrestructure.Controllers.RolesControllers.Create import CreateController

repo = MySQLRolRepository()
create_controller = CreateController(repo)
get_controller = GetController(repo)

DataRoutes = Blueprint("roles_routes", __name__)

@DataRoutes.route("/", methods=["GET"])
def get_routes():
    return get_controller.run()

@DataRoutes.route("/", methods=["POST"])
def create_route():
    return create_controller.run(request)
