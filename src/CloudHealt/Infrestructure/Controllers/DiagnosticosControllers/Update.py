from src.CloudHealt.Domain.Ports.DiagnosticoPort import DiagnosticoPort as Port
from src.CloudHealt.Application.UseCase.DiagnosticosUseCase.Update import Update as UseCase


class UpdateController:
    def __init__(self, repository: Port):
        self.use_case = UseCase(repository)

    def run(self, uuid, request):
        return self.use_case.run(uuid, request.get_json())
