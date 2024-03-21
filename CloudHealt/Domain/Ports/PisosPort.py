from abc import ABC, abstractmethod
from src.CloudHealt.Domain.Entity.Pisos import Pisos


class PisosPort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_pisos(self):
        pass

    @abstractmethod
    def create_pisos(self, piso: Pisos):
        pass
