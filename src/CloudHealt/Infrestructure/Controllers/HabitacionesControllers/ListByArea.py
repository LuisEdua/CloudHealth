from src.CloudHealt.Domain.Ports.HabitacionesPort import HabitacionesPort as Port
from src.CloudHealt.Application.UseCase.HabitacionesUseCase.ListByArea import ListByArea as UseCase


class ListByAreaController:
    def __init__(self, repository: Port):
        self.use_case = UseCase(repository)

    def run(self, area):
        return self.use_case.run(area)
