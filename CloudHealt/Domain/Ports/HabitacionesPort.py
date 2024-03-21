from abc import ABC, abstractmethod
from src.CloudHealt.Domain.Entity.Habitaciones import Habitaciones


class HabitacionesPort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_habitaciones(self, area_uuid):
        pass

    @abstractmethod
    def get_all_habitaciones(self):
        pass

    @abstractmethod
    def update_habitaciones(self, habitacion_uuid, area_uuid):
        pass

    @abstractmethod
    def create_habitaciones(self, habitaciones: list[Habitaciones]):
        pass
