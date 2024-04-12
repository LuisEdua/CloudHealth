from flask import request, Blueprint

from src.CloudHealt.Infrestructure.MiddleWares.ProtectRoutes import token_required
from src.CloudHealt.Infrestructure.Repository.MySQLTratamientoRepository import MySQLTratamientoRepository
from src.CloudHealt.Infrestructure.Controllers.TratamientosControllers.Create import CreateController
from src.CloudHealt.Infrestructure.Controllers.TratamientosControllers.Delete import DeleteController
from src.CloudHealt.Infrestructure.Controllers.TratamientosControllers.Get import GetController

repo = MySQLTratamientoRepository()
create_controller = CreateController(repo)
delete_controller = DeleteController(repo)
get_controller = GetController(repo)

DataRoutes = Blueprint("tratamientos_routes", __name__)

@DataRoutes.route("/<string:paciente_uuid>", methods=["GET"])
def get_tratamientos(paciente_uuid):
    return get_controller.run(paciente_uuid)


@DataRoutes.route("/", methods=["POST"])
@token_required
def create_tratamiento():
    return create_controller.run(request)


@DataRoutes.route("/<string:uuid>", methods=["DELETE"])
@token_required
def delete_tratamiento(uuid):
    return delete_controller.run(uuid)
