from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

from src.CloudHealt.Infrestructure.Models.MySQLHabitacionesModel import MySQLHabitacionesModel
from src.Database.MySQL import Base



class MySQLCamasModel(Base):
    __tablename__ = 'camas'
    uuid = Column(String(36), primary_key=True)
    name = Column(Integer, nullable=True)
    habitacion_uuid = Column(String(36), ForeignKey('habitaciones.uuid'), nullable=True)
    habitacion = relationship(MySQLHabitacionesModel, backref=backref('camas', uselist=True, cascade="all, delete"))

