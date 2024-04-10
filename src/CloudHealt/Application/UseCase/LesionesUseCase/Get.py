from src.CloudHealt.Domain.Ports.LessionesPort import LessionesPort as Port


class Get:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, historia_uuid):
        return self.repository.get_lesiones(historia_uuid)
