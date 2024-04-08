from src.CloudHealt.Application.UseCase.PacienteUseCase.List import List as UseCase
from src.CloudHealt.Domain.Ports.PacientesPort import PacientesPort as Port


class ListController:
    def __init__(self, repository: Port):
        self.use_case = UseCase(repository)

    def run(self, area_uuid):
        return self.use_case.run(area_uuid)
