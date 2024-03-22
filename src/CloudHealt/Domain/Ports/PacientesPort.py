from abc import ABC, abstractmethod
from src.CloudHealt.Domain.Entity.Pacientes import Pacientes


class PacientesPort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_pacientes(self, area_uuid):
        pass

    @abstractmethod
    def get_paciente(self, paciente_uuid):
        pass

    @abstractmethod
    def registerPaciente(self, paciente: Pacientes):
        pass

    @abstractmethod
    def updatePaciente(self, paciente_uuid, status, cama, quirofano):
        pass
