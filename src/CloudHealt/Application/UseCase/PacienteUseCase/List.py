from src.CloudHealt.Domain.Ports.PacientesPort import PacientesPort as Port


class List:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, area_uuid):
        return self.repository.get_pacientes(area_uuid)
