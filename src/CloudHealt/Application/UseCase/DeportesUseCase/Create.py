from src.CloudHealt.Domain.Entity.Deportes import Deportes
from src.CloudHealt.Domain.Ports.DeportesPort import DeportesPort as Port


class Create:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, datas):
        try:
            data = datas['deportes']
            historia_uuid = datas['historia_uuid']
            deportes = []

            for datos in data:
                name = datos['name']
                deporte = Deportes(name, historia_uuid)
                deportes.append(deporte)

            return self.repository.create_deportes(deportes)
        except Exception as e:
            return {'message': f'Error: {e}', "status": 'error'}, 500
