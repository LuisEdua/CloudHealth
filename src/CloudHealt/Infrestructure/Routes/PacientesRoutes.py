from flask import request, jsonify, Blueprint
from src.CloudHealt.Infrestructure.Repository.MySQLPacienteRepository import MySQLPacienteRepository
from src.CloudHealt.Infrestructure.Controllers.PacientesControllers.Create import CreateController

repo = MySQLPacienteRepository()
createController = CreateController(repo)

pacientes_routes = Blueprint('pacientes_routes', __name__)

@pacientes_routes.route('/', methods=['POST'])
def createPaciente(request):
    return jsonify(createController.run(request))
