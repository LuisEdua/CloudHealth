from src.CloudHealt.Domain.Ports.AreasPort import AreasPorts as Port


class GetAreasByFloor:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, floor_uuid):
        return self.repository.get_areas_by_floor(floor_uuid)
