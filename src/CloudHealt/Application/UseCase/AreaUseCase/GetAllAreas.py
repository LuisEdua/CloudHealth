from src.CloudHealt.Domain.Ports.AreasPort import AreasPorts as Port


class GetAllAreas:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self):
        return self.repository.get_all_areas()
