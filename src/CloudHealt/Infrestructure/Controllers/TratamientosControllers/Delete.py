from src.CloudHealt.Domain.Ports.TratamientosPort import TratamientosPort as Port
from src.CloudHealt.Application.UseCase.TratamientoUseCase.Delete import Delete as UseCase


class DeleteController:
    def __init__(self, repository: Port):
        self.use_case = UseCase(repository)

    def run(self, uuid):
        return self.use_case.run(uuid)
