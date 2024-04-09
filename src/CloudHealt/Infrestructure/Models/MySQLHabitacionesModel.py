from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from src.CloudHealt.Infrestructure.Models.MySQLAreasModel import MySQLAreasModel
from src.Database.MySQL import Base


class MySQLHabitacionesModel(Base):
    __tablename__ = 'habitaciones'
    uuid = Column(String(36), primary_key=True)
    number = Column(Integer, nullable=False)
    area_uuid = Column(String(36), ForeignKey('areas.uuid'), nullable=True)
    area = relationship(MySQLAreasModel, backref=backref('habitaciones', uselist=True, cascade="all, delete"))

    def to_json(self):
        return {
            'uuid': self.uuid,
            "number": self.number,
            "area_uuid": self.area_uuid
        }
