from src.CloudHealt.Domain.Ports.HistoriaClinicaPort import HistoriaClinicaPort as Port


class Get:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, paciente_uuid):
        return self.repository.get_historia(paciente_uuid)
