from abc import ABC, abstractmethod
from src.CloudHealt.Domain.Entity.Lesiones import Lesiones


class LessionesPort(ABC):
    @abstractmethod
    def __init__(self, lesiones: Lesiones):
        self.lesiones = lesiones

    @abstractmethod
    def get_lesiones(self, historia_uuid):
        pass

    @abstractmethod
    def create_lesiones(self, lesiones: Lesiones):
        pass
