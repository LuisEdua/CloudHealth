from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship, backref
from src.CloudHealt.Infrestructure.Models import MySQLQuirofanosModel
from src.Database.MySQL import Base
from src.CloudHealt.Infrestructure.Models.MySQLHistoriasClinicasModel import MySQLHistoriasClinicas
from src.CloudHealt.Infrestructure.Models.MySQLCamasModel import MySQLCamasModel


class MySQLPacientesModels(Base):
    __tablename__ = 'pacientes'
    uuid = Column(String(36), primary_key=True)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(20), nullable=False)
    birthday = Column(Date, nullable=False)
    quirofano_uuid = Column(String(36), ForeignKey('quirofanos.uuid'), nullable=True)
    quirofano = relationship(MySQLQuirofanosModel, backref=backref('pacientes', uselist=False))
    cama_uuid = Column(String(36), ForeignKey('camas.uuid'), nullable=True)
    cama = relationship(MySQLCamasModel, backref=backref('pacientes', uselist=False))
    historia_uuid = Column(String(36), ForeignKey('historiasclinicas.uuid'), nullable=False)
    historia = relationship(MySQLHistoriasClinicas, backref=backref('pacientes', uselist=True, cascade="all, delete"))
