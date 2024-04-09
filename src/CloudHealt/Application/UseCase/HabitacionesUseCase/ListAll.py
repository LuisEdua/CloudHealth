from src.CloudHealt.Domain.Ports.HabitacionesPort import HabitacionesPort as Port


class ListAll:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self):
        return self.repository.get_all_habitaciones()

