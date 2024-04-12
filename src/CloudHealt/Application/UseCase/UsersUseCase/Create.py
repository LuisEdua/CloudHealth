from src.CloudHealt.Domain.Ports.UsersPort import UsersPort as Port
from src.CloudHealt.Domain.Entity.Users import Users


class Create:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, data):
        try:
            firstname = data['firstname']
            lastname = data['lastname']
            email = data['email']
            password = data['password']
            rol_uuid = data['rol_uuid']
            area_uuid = data['area_uuid']
            birthday = data['birthday']
            age = int(data['age'])
            user = Users(firstname, lastname, email, password, rol_uuid, area_uuid, age, birthday)
            return self.repository.create(user)
        except Exception as e:
            return {"Message": f"Something went wrong \n{e}", "Status": "Error"}, 500
