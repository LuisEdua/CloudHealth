from src.CloudHealt.Application.UseCase.PacienteUseCase.Create import Create as UseCase
from src.CloudHealt.Domain.Ports.PacientesPort import PacientesPort as Port


class CreateController:
    def __init__(self, repository: Port):
        self.use_case = UseCase(repository)

    def run(self, data):
        return self.use_case.run(data.get_json())
