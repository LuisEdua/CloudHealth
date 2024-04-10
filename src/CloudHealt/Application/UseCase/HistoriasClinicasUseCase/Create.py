from src.CloudHealt.Domain.Ports.HistoriaClinicaPort import HistoriaClinicaPort as Port
from src.CloudHealt.Domain.Entity.HistoriasClinicas import HistoriasClinicas


class Create:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, data):
        try:
            profesion = data['profesion']
            weight = data['weight']
            high = data['high']
            historia = HistoriasClinicas(profesion, weight, high)
            return self.repository.create_historia(historia)
        except Exception as e:
            return {"Message": f'Error: {e}', 'status': "error"}, 500
