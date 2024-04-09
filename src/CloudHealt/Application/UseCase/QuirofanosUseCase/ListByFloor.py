from src.CloudHealt.Domain.Ports.QuirofanosPort import QuirofanosPort as Port


class ListByFloor:
    def __init__(self, repository:Port):
        self.repository = repository

    def run(self, floor_uuid):
        return self.repository.get_quirofanos(floor_uuid)
