from src.CloudHealt.Application.UseCase.PisosUseCase.Get import Get as UseCase
from src.CloudHealt.Domain.Ports.PisosPort import PisosPort as Port


class GetController:
    def __init__(self, repository: Port):
        self.use_case = UseCase(repository)

    def run(self):
        return self.use_case.run()
