from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from src.Database.MySQL import Base
from src.CloudHealt.Infrestructure.Models.MySQLHistoriasClinicasModel import MySQLHistoriasClinicas


class MySQLDeportesModel(Base):
    __tablename__ = 'deportes'
    uuid = Column(String(36), primary_key=True)
    name = Column(String(255), nullable=False)
    historia_uuid = Column(String(36), ForeignKey('historiasclinicas.uuid'))
    historia = relationship(MySQLHistoriasClinicas, backref=backref('deportes', uselist=True, cascade="all, delete"))
