from flask import request, jsonify, Blueprint
from src.CloudHealt.Infrestructure.Controllers.HistoriasClinicasControllers.Create import CreateController
from src.CloudHealt.Infrestructure.Repository.MySQLHistoriasClinicasRepository import MySQLHistoriasClinicasRepository
from src.CloudHealt.Infrestructure.Controllers.HistoriasClinicasControllers.Get import GetController

repo = MySQLHistoriasClinicasRepository()
create_controller = CreateController(repo)
get_controller = GetController(repo)

historias_routes = Blueprint('historias_routes', __name__)

@historias_routes.route('/<string:paciente_uuid>', methods=['GET'])
def get_routes(paciente_uuid):
    return get_controller.run(paciente_uuid)

@historias_routes.route('/', methods=['POST'])
def create_route():
    return create_controller.run(request)

