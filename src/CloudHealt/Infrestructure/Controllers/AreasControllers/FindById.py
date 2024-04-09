from src.CloudHealt.Application.UseCase.AreaUseCase.GetAreasById import GetAreasById as UseCase
from src.CloudHealt.Domain.Ports.AreasPort import AreasPorts as Port


class FindByIdController:
    def __init__(self, repository: Port):
        self.use_case = UseCase(repository)

    def run(self, uuid):
        return self.use_case.run(uuid)
