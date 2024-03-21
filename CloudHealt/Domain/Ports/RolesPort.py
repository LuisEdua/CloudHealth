from abc import ABC, abstractmethod
from src.CloudHealt.Domain.Entity.Roles import Roles


class RolesPort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_roles(self):
        pass

    @abstractmethod
    def create_role(self, rol: Roles):
        pass
