from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from uuid import uuid4
from src.CloudHealt.Infrestructure.Models.MySQLAreasModel import MySQLAreasModel
from src.Database.MySQL import Base


class MySQLHabitacionesModel(Base):
    __tablename__ = 'habitaciones'
    uuid = Column(String(36), primary_key=True, default=uuid4())
    number = Column(Integer, nullable=False)
    area_uuid = Column(String(36), ForeignKey('areas.uuid'), nullable=False)
    area = relationship(MySQLAreasModel, backref=backref('habitaciones', uselist=True, cascade="all, delete"))

