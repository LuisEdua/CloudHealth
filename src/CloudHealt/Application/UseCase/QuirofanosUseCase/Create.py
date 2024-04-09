from src.CloudHealt.Domain.Ports.QuirofanosPort import QuirofanosPort as Port
from src.CloudHealt.Domain.Entity.Quirofanos import Quirofanos


class Create:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, data):
        try:
            number = data['number']
            description = data['description']
            floor_uuid = data['floor_uuid']
            quirofano = Quirofanos(number, description, floor_uuid)
            return self.repository.create_quirofanos(quirofano)
        except Exception as e:
            return {"message": str(e), "status": "error"}, 500
