from src.CloudHealt.Application.UseCase.AreaUseCase.GetAllAreas import GetAllAreas as UseCase
from src.CloudHealt.Domain.Ports.AreasPort import AreasPorts as Port


class ListAllController:
    def __init__(self, repository: Port):
        self.use_case = UseCase(repository)

    def run(self):
        return self.use_case.run()
