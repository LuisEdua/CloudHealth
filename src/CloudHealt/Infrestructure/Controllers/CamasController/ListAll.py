from src.CloudHealt.Application.UseCase.CamaUseCase.ListAll import ListAll as UseCase
from src.CloudHealt.Domain.Ports.CamasPort import CamasPort as Port


class ListAllController:
    def __init__(self, repository: Port):
        self.use_case = UseCase(repository)

    def run(self):
        return self.use_case.run()
