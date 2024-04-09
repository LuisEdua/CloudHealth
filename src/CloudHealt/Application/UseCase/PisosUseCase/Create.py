from src.CloudHealt.Domain.Ports.PisosPort import PisosPort as Port
from src.CloudHealt.Domain.Entity.Pisos import Pisos


class Create:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, data):
        try:
            level= data['level']
            piso = Pisos(level)
            return self.repository.create_pisos(piso)
        except Exception as e:
            return {"message": "Unexpected error: " + str(e), "status": "error"}, 500
