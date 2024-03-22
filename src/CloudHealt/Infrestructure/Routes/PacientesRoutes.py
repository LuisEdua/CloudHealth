from flask import request, jsonify, Blueprint
from src.CloudHealt.Infrestructure.Repository.MySQLPacienteRepository import MySQLPacienteRepository
from src.CloudHealt.Infrestructure.Controllers.PacientesControllers.List import ListController

repo = MySQLPacienteRepository()
listController = ListController(repo)

pacientes_routes = Blueprint('pacientes_routes', __name__)


@pacientes_routes.route('/area/<string:area_uuid>', methods=['GET'])
def list_pacientes(area_uuid):
    return listController.run(area_uuid)

