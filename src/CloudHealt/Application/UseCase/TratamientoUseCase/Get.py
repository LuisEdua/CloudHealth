from src.CloudHealt.Domain.Ports.TratamientosPort import TratamientosPort as Port


class Get:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, paciente_uuid):
        return self.repository.get_tratamientos(paciente_uuid)
