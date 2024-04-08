from src.CloudHealt.Application.UseCase.PacienteUseCase.FindById import FindById as UseCase
from src.CloudHealt.Domain.Ports.PacientesPort import PacientesPort as Port


class FindByIdController(UseCase):
    def __init__(self, repository: Port):
        self.use_case = UseCase(repository)

    def run(self, uuid):
        try:
            return self.use_case.run(uuid)
        except Exception as e:
            error_message = "System interruption"
            return {"error": error_message, 'status': 'Interrumpted'}
