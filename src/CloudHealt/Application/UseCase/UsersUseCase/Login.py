from src.CloudHealt.Domain.Ports.UsersPort import UsersPort as Port


class Login:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, data):
        try:
            email = str(data['email'])
            password = str(data['password'])
            return self.repository.login(email, password)
        except Exception as e:
            return {"Message": f"Something went wrong \n{e}", "status": "error"}, 500
