from src.CloudHealt.Domain.Ports.DiagnosticoPort import DiagnosticoPort as Port


class Delete:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, uuid):
        return self.repository.delete_diagnostico(uuid)
