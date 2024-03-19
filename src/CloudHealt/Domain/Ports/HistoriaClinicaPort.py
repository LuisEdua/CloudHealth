from abc import ABC, abstractmethod
from src.CloudHealt.Domain.Entity.HistoriasClinicas import HistoriasClinicas


class HistoriaClinicaPort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_historia(self, paciente_uuid):
        pass

    @abstractmethod
    def create_historia(self, historia: HistoriasClinicas):
        pass
