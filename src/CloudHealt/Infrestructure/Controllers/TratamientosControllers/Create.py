from src.CloudHealt.Domain.Ports.TratamientosPort import TratamientosPort as Port
from src.CloudHealt.Application.UseCase.TratamientoUseCase.Create import Create as UseCase


class CreateController:
    def __init__(self, repository: Port):
        self.use_case = UseCase(repository)

    def run(self, request):
        return self.use_case.run(request.get_json())
