from src.CloudHealt.Domain.Ports.TratamientosPort import TratamientosPort as Port
from src.CloudHealt.Domain.Entity.Tratamientos import Tratamientos


class Create:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, data):
        try:
            title = data['title']
            description = data['description']
            paciente_uuid = data['paciente_uuid']
            tratamiento = Tratamientos(title, description, paciente_uuid)
            return self.repository.create_tratamiento(tratamiento)
        except Exception as e:
            return {"Message": f'Error: {e}', "status": "error"}, 500
