from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from src.CloudHealt.Infrestructure.Models.MySQLPisosModel import MySQLPisosModel
from src.Database.MySQL import Base
from uuid import uuid4

class MySQLAreasModel(Base):
    __tablename__ = 'areas'
    uuid = Column(String(36), primary_key=True, default=uuid4())
    name = Column(String(255), nullable=False)
    floor_uuid = Column(String(36), ForeignKey('floor.uuid'), nullable=False)
    floor = relationship(MySQLPisosModel, backref=backref('areas', uselist=True, cascade="all, delete"))
