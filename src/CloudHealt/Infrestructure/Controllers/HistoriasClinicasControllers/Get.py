from src.CloudHealt.Application.UseCase.HistoriasClinicasUseCase.Get import Get as UseCase
from src.CloudHealt.Domain.Ports.HistoriaClinicaPort import HistoriaClinicaPort as Port


class GetController:
    def __init__(self, repository: Port):
        self.use_case = UseCase(repository)

    def run(self, paciente_uuid):
        return self.use_case.run(paciente_uuid)
