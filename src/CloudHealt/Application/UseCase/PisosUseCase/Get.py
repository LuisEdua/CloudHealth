from src.CloudHealt.Domain.Ports.PisosPort import PisosPort as Port


class Get:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self):
        return self.repository.get_pisos()
