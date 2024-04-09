from src.CloudHealt.Domain.Ports.HabitacionesPort import HabitacionesPort as Port


class ListByArea:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, area):
        return self.repository.get_habitaciones(area)
