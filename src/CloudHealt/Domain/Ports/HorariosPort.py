from abc import ABC, abstractmethod
from src.CloudHealt.Domain.Entity.Horarios import Horarios


class HorariosPort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_horarios(self, tratamiento_uuid):
        pass

    def create_horarios(self, horario: Horarios):
        pass
