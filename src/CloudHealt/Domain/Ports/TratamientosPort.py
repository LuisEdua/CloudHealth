from abc import ABC, abstractmethod
from src.CloudHealt.Domain.Entity.Tratamientos import Tratamientos


class TratamientosPort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_tratamientos(self, paciente_uuid):
        pass

    @abstractmethod
    def create_tratamiento(self, tratamiento: Tratamientos):
        pass

    @abstractmethod
    def delete_tratamiento(self, uuid):
        pass
