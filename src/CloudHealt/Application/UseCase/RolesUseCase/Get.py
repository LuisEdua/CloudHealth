from src.CloudHealt.Domain.Ports.RolesPort import RolesPort as Port


class Get:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self):
        return self.repository.get_roles()
