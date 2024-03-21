from flask import request, jsonify, Blueprint
from src.CloudHealt.Infrestructure.Repository.MySQLPacienteRepository import MySQLPacienteRepository
from src.CloudHealt.Infrestructure.Controllers.PacientesControllers.FindByIDController import FindByIdController

repo = MySQLPacienteRepository()
findByIdController = FindByIdController(repo)

pacientes_routes = Blueprint('pacientes_routes', __name__)

@pacientes_routes.route('/<string:uuid>', methods=['GET'])
def findById(uuid):
    response = findByIdController.run(uuid)
    status_code = 404
    if response['status'] == 'Success':
        status_code = 200
    elif response['status'] == 'Interrumpted':
        status_code = 500
    return jsonify(response), status_code

