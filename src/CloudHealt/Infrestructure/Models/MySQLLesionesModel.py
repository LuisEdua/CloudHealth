from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from src.Database.MySQL import Base
from src.CloudHealt.Infrestructure.Models.MySQLHistoriasClinicasModel import MySQLHistoriasClinicas


class MySQLLesionesModel(Base):
    __tablename__ = 'lesiones'
    uuid = Column(String(36), primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(String(255), nullable=False)
    historia_uuid = Column(String(36), ForeignKey('historiasclinicas.uuid'), nullable=False)
    historia = relationship(MySQLHistoriasClinicas, backref=backref('deportes', uselist=True, cascade="all, delete"))
