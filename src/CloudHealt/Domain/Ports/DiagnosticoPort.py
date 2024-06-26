from abc import ABC, abstractmethod
from src.CloudHealt.Domain.Entity.Diagnosticos import Diagnosticos


class DiagnosticoPort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_diagnosticos(self, paciente_uuid):
        pass

    @abstractmethod
    def create_diagnostico(self, diagnostico: Diagnosticos):
        pass

    @abstractmethod
    def update_diagnostico(self, uuid, title: str, description: str):
        pass

    @abstractmethod
    def delete_diagnostico(self, uuid: str):
        pass
