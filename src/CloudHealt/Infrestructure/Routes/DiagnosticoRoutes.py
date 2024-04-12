from flask import request, Blueprint

from src.CloudHealt.Infrestructure.MiddleWares.ProtectRoutes import token_required
from src.CloudHealt.Infrestructure.Repository.MySQLDiagnosticoRepository import MySQLDiagnosticoRepository
from src.CloudHealt.Infrestructure.Controllers.DiagnosticosControllers.Create import CreateController
from src.CloudHealt.Infrestructure.Controllers.DiagnosticosControllers.Get import GetController
from src.CloudHealt.Infrestructure.Controllers.DiagnosticosControllers.Delete import DeleteController
from src.CloudHealt.Infrestructure.Controllers.DiagnosticosControllers.Update import UpdateController

repo = MySQLDiagnosticoRepository()
create_controller = CreateController(repo)
delete_controller = DeleteController(repo)
get_controller = GetController(repo)
update_controller = UpdateController(repo)


DataRoutes = Blueprint("diagnostico_routes", __name__)

@DataRoutes.route("/<string:paciente_uuid>", methods=["GET"])
def get_diagnosticos(paciente_uuid):
    return get_controller.run(paciente_uuid)


@DataRoutes.route("/", methods=["POST"])
@token_required
def create_diagnostico():
    return create_controller.run(request)


@DataRoutes.route("/<string:uuid>", methods=["PUT"])
@token_required
def update_diagnostico(uuid):
    return update_controller.run(uuid, request)

@DataRoutes.route("/<string:uuid>", methods=["DELETE"])
@token_required
def delete_diagnostico(uuid):
    return delete_controller.run(uuid)
