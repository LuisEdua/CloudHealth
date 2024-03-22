from src.CloudHealt.Application.UseCase.PacienteUseCase.Update import Update as UseCase
from src.CloudHealt.Domain.Ports.PacientesPort import PacientesPort as Port


class UpdateController:
    def __init__(self, repository: Port):
        self.use_case = UseCase(repository)

    def run(self, paciente_uuid, data):
        return self.use_case.run(data.get_json(), paciente_uuid)