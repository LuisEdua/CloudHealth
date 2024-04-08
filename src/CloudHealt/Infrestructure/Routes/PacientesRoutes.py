from flask import request, jsonify, Blueprint
from src.CloudHealt.Infrestructure.Repository.MySQLPacienteRepository import MySQLPacienteRepository
from src.CloudHealt.Infrestructure.Controllers.PacientesControllers.Create import CreateController

repo = MySQLPacienteRepository()
createController = CreateController(repo)

pacientes_routes = Blueprint('pacientes_routes', __name__)

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
