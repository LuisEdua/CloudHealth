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
    def login(self, username: str, password: str):
        pass

    @abstractmethod
    def create(self, user: Users):
        pass

    @abstractmethod
    def update_user(self, email=None, password=None, area_uuid=None):
        pass
