from src.CloudHealt.Domain.Ports.RolesPort import RolesPort as Port
from src.CloudHealt.Application.UseCase.RolesUseCase.Create import Create as UseCase


class CreateController:
    def __init__(self, repository: Port):
        self.use_case = UseCase(repository)

    def run(self, request):
        return self.use_case.run(request.get_json())
