from src.CloudHealt.Domain.Ports.PacientesPort import PacientesPort as Port
from src.CloudHealt.Domain.Entity.Pacientes import Pacientes


class FindById:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, id: str):
        return self.repository.get_paciente(id)
