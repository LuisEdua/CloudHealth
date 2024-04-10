from src.CloudHealt.Domain.Ports.UsersPort import UsersPort as Port
from src.CloudHealt.Application.UseCase.UsersUseCase.GetByArea import GetByArea as UseCase


class GetByAreaController:
    def __init__(self, repository: Port):
        self.use_case = UseCase(repository)

    def run(self, area_uuid):
        return self.use_case.run(area_uuid)
