from abc import ABC, abstractmethod
from src.CloudHealt.Domain.Entity.Quirofanos import Quirofanos


class QuirofanosPort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_all_quirofanos(self):
        pass

    @abstractmethod
    def get_quirofanos(self, floor_uuid):
        pass

    @abstractmethod
    def create_quirofanos(self, quirofano: Quirofanos):
        pass
