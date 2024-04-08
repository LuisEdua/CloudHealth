from flask import request, jsonify, Blueprint
from src.CloudHealt.Infrestructure.Repository.MySQLPacienteRepository import MySQLPacienteRepository
from src.CloudHealt.Infrestructure.Controllers.PacientesControllers.List import ListController
from src.CloudHealt.Infrestructure.Controllers.PacientesControllers.Create import CreateController

repo = MySQLPacienteRepository()
listController = ListController(repo)
createController = CreateController(repo)

pacientes_routes = Blueprint('pacientes_routes', __name__)

@pacientes_routes.route('/area/<string:area_uuid>', methods=['GET'])
def list_pacientes(area_uuid):
    return listController.run(area_uuid)

@pacientes_routes.route('/', methods=['POST'])
def create_paciente():
    result = createController.run(request)
    if result['status'] == 'Created':
        return jsonify(result), 201
    elif result['status'] == 'Failed':
        return jsonify(result), 400
    elif result['status'] == 'Interrupted':
        return jsonify(result), 500
    else:
        return jsonify({'message': 'Resultado desconocido'}), 500
