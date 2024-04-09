from src.CloudHealt.Application.UseCase.AreaUseCase.GetAreasByFloor import GetAreasByFloor as UseCase
from src.CloudHealt.Domain.Ports.AreasPort import AreasPorts as Port


class ListByFloorController:
    def __init__(self, repository: Port):
        self.use_case = UseCase(repository)

    def run(self, floor_uuid):
        return self.use_case.run(floor_uuid)
