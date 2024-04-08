from src.CloudHealt.Application.UseCase.CamaUseCase.ListFree import ListFree as UseCase
from src.CloudHealt.Domain.Ports.CamasPort import CamasPort as Port


class ListFreeController:
    def __init__(self, repository: Port):
        self.use_case = UseCase(repository)

    def run(self, area_uuid):
        return self.use_case.run(area_uuid)
