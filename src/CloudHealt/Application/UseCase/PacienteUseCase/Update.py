from src.CloudHealt.Domain.Ports.PacientesPort import PacientesPort as Port


class Update:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, data, paciente_uuid):
        status = data['status']
        cama = data['cama']
        quirofano = data['quirofano']
        return self.repository.updatePaciente(paciente_uuid, status, cama, quirofano)

