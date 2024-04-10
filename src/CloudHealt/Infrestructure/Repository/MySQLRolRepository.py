from src.CloudHealt.Domain.Entity.Roles import Roles
from src.CloudHealt.Domain.Ports.RolesPort import RolesPort
from src.Database.MySQL import Base, session_local, engine
from src.CloudHealt.Infrestructure.Models.MySQLRolesModel import MySQLRolesModel as Model


class MySQLRolRepository(RolesPort):
    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.db = session_local()

    def get_roles(self):
        try:
            roles = self.db.query(Model).all()
            if roles:
                return {"Message": "Roles found", "Roles": [rol.to_json() for rol in roles],
                        "status": "Success"}, 200
            else:
                return {"Message": "Roles not found", "status": "not found"}, 404
        except Exception as e:
            return {"Message": f"Something went wrong \n{e}", "status": "error"}, 500

    def create_role(self, rol: Roles):
        try:
            new = Model(name=rol.name, uuid=rol.uuid)
            self.db.add(new)
            self.db.commit()
            return {"Message": "Role created", "rol": new.to_json()}, 201
        except Exception as e:
            return {"Message": f"Something went wrong \n{e}", "status": "error"}, 500