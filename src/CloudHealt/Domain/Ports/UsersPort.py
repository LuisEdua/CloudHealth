from abc import ABC, abstractmethod
from src.CloudHealt.Domain.Entity.Users import Users


class UsersPort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_users(self):
        pass

    @abstractmethod
    def get_users_by_area(self, area_uuid):
        pass


    @abstractmethod
    def login(self, email: str, password: str):
        pass

    @abstractmethod
    def create(self, user: Users):
        pass

    @abstractmethod
    def update_user(self, uuid:str, email=None, password=None, area_uuid=None):
        pass

    @abstractmethod
    def delete_user(self, uuid:str):
        pass
