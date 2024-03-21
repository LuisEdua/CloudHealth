from flask import request, jsonify, Blueprint
from src.CloudHealt.Infrestructure.Controllers.HistoriasClinicasControllers.Create import CreateController
from src.CloudHealt.Infrestructure.Repository.MySQLHistoriasClinicasRepository import MySQLHistoriasClinicasRepository

repo = MySQLHistoriasClinicasRepository()
create_controller = CreateController(repo)

historias_routes = Blueprint('historias_routes', __name__)

@historias_routes.route('/', methods=['POST'])
def create_route():
    return jsonify(create_controller.run(request)), 201

