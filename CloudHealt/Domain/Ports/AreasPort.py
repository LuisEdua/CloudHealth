from abc import ABC, abstractmethod
from src.CloudHealt.Domain.Entity.Areas import Areas


class AreasPorts(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_areas_by_id(self, area_uuid):
        pass

    @abstractmethod
    def get_areas_by_floor(self, floor_uuid):
        pass

    @abstractmethod
    def get_all_areas(self):
        pass

    @abstractmethod
    def create_area(self, area: Areas):
        pass
