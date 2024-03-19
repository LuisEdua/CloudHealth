from abc import ABC, abstractmethod
from src.CloudHealt.Domain.Entity.Pacientes import Pacientes


class PacientesPort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def getPacientes(self, level_uuid):
        pass

    @abstractmethod
    def getPaciente(self, paciente_uuid):
        pass

    @abstractmethod
    def registerPaciente(self, paciente: Pacientes):
        pass

    @abstractmethod
    def updatePaciente(self, status, cama):
        pass
