from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from src.CloudHealt.Infrestructure.Models.MySQLPisosModel import MySQLPisosModel
from src.Database.MySQL import Base
from uuid import uuid4

class MySQLQuirofanos(Base):
    __tablename__ = 'quirofanos'
    uuid = Column(String(36), primary_key=True, default=uuid4())
    number = Column(Integer, nullable=False)
    description = Column(String(255), nullable=False)
    floor_uuid = Column(String(36), ForeignKey('floor.uuid'), nullable=False)
    paciente_uuid = Column(String(36), ForeignKey('pacientes.uuid'))
    floor = relationship(MySQLPisosModel, backref=backref('quirofanos', uselist=True, cascade="all, delete"))
