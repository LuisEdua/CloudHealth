from src.CloudHealt.Domain.Ports.HabitacionesPort import HabitacionesPort as Port
from src.CloudHealt.Application.UseCase.HabitacionesUseCase.Create import Create as UseCase


class CreateController:
    def __init__(self, repository: Port):
        self.use_case = UseCase(repository)

    def run(self, data):
        return self.use_case.run(data.get_json())

