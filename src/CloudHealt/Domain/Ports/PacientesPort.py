from abc import ABC, abstractmethod
from src.CloudHealt.Domain.Entity.Pacientes import Pacientes


class PacientesPorts(ABC):

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
