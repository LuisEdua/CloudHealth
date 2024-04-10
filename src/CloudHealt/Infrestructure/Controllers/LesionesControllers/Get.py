from src.CloudHealt.Domain.Ports.LessionesPort import LessionesPort as Port
from src.CloudHealt.Application.UseCase.LesionesUseCase.Get import Get as UseCase


class GetController:
    def __init__(self, repository: Port):
        self.use_case = UseCase(repository)

    def run(self, historia_uuid):
        return self.use_case.run(historia_uuid)
