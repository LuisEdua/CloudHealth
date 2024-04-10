from src.CloudHealt.Domain.Entity.Roles import Roles
from src.CloudHealt.Domain.Ports.RolesPort import RolesPort as Port


class Create:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, data):
        try:
            name = data['name']
            rol = Roles(name)
            return self.repository.create_role(rol)
        except Exception as e:
            return {"Message": f"Something went wrong \n{e}", "status": "error"}, 500
