from src.CloudHealt.Domain.Ports.UsersPort import UsersPort as Port


class GetAll:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self):
        return self.repository.get_users()
