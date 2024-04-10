from src.CloudHealt.Domain.Ports.UsersPort import UsersPort as Port


class Delete:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, user_uuid):
        return self.repository.delete_user(user_uuid)
