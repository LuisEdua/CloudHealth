from src.CloudHealt.Domain.Ports.DiagnosticoPort import DiagnosticoPort as Port


class Get:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, paciente_uuid):
        return self.repository.get_diagnosticos(paciente_uuid)
