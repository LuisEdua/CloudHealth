from abc import ABC, abstractmethod
from src.CloudHealt.Domain.Entity.Deportes import Deportes


class DeportesPort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_deportes(self, historia_uuid):
        pass

    @abstractmethod
    def create_deportes(self, deporte: Deportes):
        pass