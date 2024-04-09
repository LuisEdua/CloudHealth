from src.CloudHealt.Domain.Entity.Areas import Areas
from src.CloudHealt.Domain.Ports.AreasPort import AreasPorts as Port


class Create:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, data):
        try:
            name = data['name']
            floor_uuid = data['floor_uuid']
            area = Areas(name, floor_uuid)
            return self.repository.create_area(area)
        except Exception as e:
            return {"message": str(e), "status": "error"}, 500
