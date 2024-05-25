from flask import request, Blueprint

from src.CloudHealt.Infrestructure.MiddleWares.ProtectRoutes import token_required
from src.CloudHealt.Infrestructure.Repository.MySQLUsuariosRepository import MySQLUsuariosRepository
from src.CloudHealt.Infrestructure.Controllers.UsersControllers.Create import CreateController
from src.CloudHealt.Infrestructure.Controllers.UsersControllers.Update import UpdateController
from src.CloudHealt.Infrestructure.Controllers.UsersControllers.GetAll import GetAllController
from src.CloudHealt.Infrestructure.Controllers.UsersControllers.Login import LoginController
from src.CloudHealt.Infrestructure.Controllers.UsersControllers.GetByArea import GetByAreaController
from src.CloudHealt.Infrestructure.Controllers.UsersControllers.Delete import DeleteController

repo = MySQLUsuariosRepository()
create_controller = CreateController(repo)
update_controller = UpdateController(repo)
get_all_controller = GetAllController(repo)
get_by_area_controller = GetByAreaController(repo)
login_controller = LoginController(repo)
delete_controller = DeleteController(repo)

DataRoutes = Blueprint("users_routes", __name__)

@DataRoutes.route('/', methods=['GET'])
def get_all():
    return get_all_controller.run()


@DataRoutes.route('/<string:area_uuid>', methods=['GET'])
def get_by_area(area_uuid):
    return get_by_area_controller.run(area_uuid)


@DataRoutes.route('/', methods=["POST"])
def create():
    return create_controller.run(request)


@DataRoutes.route('/login', methods=["POST"])
def login():
    return login_controller.run(request)


@DataRoutes.route('/<string:uuid>', methods=["PUT"])
def update(uuid):
    return update_controller.run(uuid, request)

@DataRoutes.route('/<string:uuid>', methods=["DELETE"])
def delete(uuid):
    return delete_controller.run(uuid)
