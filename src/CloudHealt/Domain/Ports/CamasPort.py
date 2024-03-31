from abc import ABC, abstractmethod
from src.CloudHealt.Domain.Entity.Camas import Camas


class CamasPort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_free_camas(self, area_uuid):
        pass

    @abstractmethod
    def get_all_camas(self):
        pass

    @abstractmethod
    def create_camas(self, camas: list[Camas]):
        pass
