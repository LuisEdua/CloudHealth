from src.CloudHealt.Domain.Ports.UsersPort import UsersPort as Port


class Update:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, uuid,data):
        try:
            email = data['email']
            password = data['password']
            area = data['area_uuid']
            return self.repository.update_user(uuid, email, password, area)
        except Exception as e:
            return {"Message": f"Something went wrong \n{e}", "status": "error"}, 500
