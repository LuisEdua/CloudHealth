from src.CloudHealt.Domain.Ports.DiagnosticoPort import DiagnosticoPort as Port
from src.CloudHealt.Application.UseCase.DiagnosticosUseCase.Delete import Delete as UseCase


class DeleteController:
    def __init__(self, repository: Port):
        self.use_case = UseCase(repository)

    def run(self, uuid):
        return self.use_case.run(uuid)
