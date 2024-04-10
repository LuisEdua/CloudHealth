from src.CloudHealt.Domain.Ports.TratamientosPort import TratamientosPort as Port


class Delete:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, uuid):
        return self.repository.delete_tratamiento(uuid)

