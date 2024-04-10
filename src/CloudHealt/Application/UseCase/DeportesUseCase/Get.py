from src.CloudHealt.Domain.Ports.DeportesPort import DeportesPort as Port


class Get:
    def __init__(self, repository: Port):
        self.repository = repository


    def run(self, historia_uuid):
        return self.repository.get_deportes(historia_uuid)
