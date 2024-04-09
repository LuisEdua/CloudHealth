from src.CloudHealt.Domain.Ports.CamasPort import CamasPort as Port
from src.CloudHealt.Domain.Entity.Camas import Camas


class Create:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, data):
        try:
            camas = []
            cantidad = data['cantidad']
            habitacion = data['habitacion']
            for i in range(1, cantidad + 1):
                cama= Camas(i, habitacion)
                camas.append(cama)
            return self.repository.create_camas(camas)
        except Exception as e:
            return {"error": str(e), "status": "Unexpected data"}, 500
