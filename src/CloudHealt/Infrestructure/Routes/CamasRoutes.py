from flask import Blueprint, jsonify, request
from src.CloudHealt.Infrestructure.Controllers.CamasControllers.Create import CreateController
from src.CloudHealt.Infrestructure.Controllers.CamasControllers.ListFree import ListFreeController
from src.CloudHealt.Infrestructure.Controllers.CamasControllers.ListAll import ListAllController
from src.CloudHealt.Infrestructure.Repository.MySQLCamaRepository import MySQLCamasRepository

repo = MySQLCamasRepository()
create_controller = CreateController(repo)
list_free_controller = ListFreeController(repo)
list_all_controller = ListAllController(repo)

camas_routes = Blueprint('camas_routes', __name__)

@camas_routes.route('/', methods=['GET'])
def get_all_camas():
    return jsonify(list_all_controller.run())

@camas_routes.route('/<string:area_uuid>', methods=['GET'])
def get_free_camas(area_uuid):
    return jsonify(list_free_controller.run(area_uuid))

@camas_routes.route('/', methods=['POST'])
def create_camas():
    return jsonify(create_controller.run(request))
