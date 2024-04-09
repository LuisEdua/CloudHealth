from src.CloudHealt.Domain.Ports.AreasPort import AreasPorts as Port


class GetAreasById:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, area_uuid):
        return self.repository.get_areas_by_id(area_uuid)
