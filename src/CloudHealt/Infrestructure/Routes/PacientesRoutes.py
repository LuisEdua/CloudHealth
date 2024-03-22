from flask import request, jsonify, Blueprint
from src.CloudHealt.Infrestructure.Repository.MySQLPacienteRepository import MySQLPacienteRepository
from src.CloudHealt.Infrestructure.Controllers.PacientesController.Update import UpdateController

repo = MySQLPacienteRepository()
updateController = UpdateController(repo)


pacientes_routes = Blueprint('pacientes_routes', __name__)


@pacientes_routes.route('/<string:paciente_uuid>', methods=['PUT'])
def update(paciente_uuid):
    return updateController.run(paciente_uuid, request)
