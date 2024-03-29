from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship, backref
from src.Database.MySQL import Base
from src.CloudHealt.Infrestructure.Models.MySQLTratamientosModel import MySQLTratamientosModel


class MySQLHorariosModel(Base):
    __tablename__ = 'horarios'
    uuid = Column(String(36), primary_key=True)
    hora = Column(Integer, nullable=False)
    minuto = Column(Integer, nullable=False)
    inicio = Column(Date, nullable=False)
    final = Column(Date, nullable=False)
    tratamiento_uuid = Column(String(36), ForeignKey('tratamientos.id'), nullable=False)
    tratamiento = relationship(MySQLTratamientosModel, backref=backref('horarios', useList=True, cascade="all, delete"))
