from src.CloudHealt.Domain.Ports.HabitacionesPort import HabitacionesPort as Port
from src.CloudHealt.Application.UseCase.HabitacionesUseCase.ListAll import ListAll as UseCase


class ListAllController:
    def __init__(self, repository: Port):
        self.use_case = UseCase(repository)

    def run(self):
        return self.use_case.run()
