from src.CloudHealt.Domain.Ports.DiagnosticoPort import DiagnosticoPort as Port
from src.CloudHealt.Application.UseCase.DiagnosticosUseCase.Get import Get as UseCase


class GetController:
    def __init__(self, repository: Port):
        self.use_case = UseCase(repository)

    def run(self, paciente_uuid):
        return self.use_case.run(paciente_uuid)
