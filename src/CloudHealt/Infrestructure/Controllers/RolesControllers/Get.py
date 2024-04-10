from src.CloudHealt.Domain.Ports.RolesPort import RolesPort as Port
from src.CloudHealt.Application.UseCase.RolesUseCase.Get import Get as UseCase


class GetController:
    def __init__(self, repository: Port):
        self.use_case = UseCase(repository)

    def run(self):
        return self.use_case.run()
