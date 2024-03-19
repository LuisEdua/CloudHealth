from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship, backref
from src.Database.MySQL import Base
from src.CloudHealt.Infrestructure.Models.MySQLHistoriasClinicasModel import MySQLHistoriasClinicas


class MySQLPacientesModels(Base):
    __tablename__ = 'pacientes'
    uuid = Column(String(36), primary_key=True)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(20), nullable=False)
    birthday = Column(Date, nullable=False)
    historia_uuid = Column(String(36), ForeignKey('historiasclinicas.uuid'))
    historia = relationship(MySQLHistoriasClinicas, backref=backref('pacientes', uselist=True, cascade="all, delete"))
