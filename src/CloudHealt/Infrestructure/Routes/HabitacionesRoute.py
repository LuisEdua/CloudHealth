from flask import request, Blueprint

from src.CloudHealt.Infrestructure.MiddleWares.ProtectRoutes import token_required
from src.CloudHealt.Infrestructure.Repository.MySQLHabitacionRepository import MySQLHabitacionRepository
from src.CloudHealt.Infrestructure.Controllers.HabitacionesControllers.Create import CreateController
from src.CloudHealt.Infrestructure.Controllers.HabitacionesControllers.ListAll import ListAllController
from src.CloudHealt.Infrestructure.Controllers.HabitacionesControllers.ListByArea import ListByAreaController

repo = MySQLHabitacionRepository()
create_controller = CreateController(repo)
list_all_controller = ListAllController(repo)
list_by_area_controller = ListByAreaController(repo)

DataRoutes = Blueprint("habitaciones_routes", __name__)


@DataRoutes.route("/", methods=["GET"])
@token_required
def list_all():
    return list_all_controller.run()


@DataRoutes.route("/<string:area_id>", methods=["GET"])
@token_required
def list_by_area(area_id):
    return list_by_area_controller.run(area_id)


@DataRoutes.route("/", methods=["POST"])
@token_required
def create():
    return create_controller.run(request)
