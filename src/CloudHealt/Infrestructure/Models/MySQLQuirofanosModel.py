from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from src.CloudHealt.Infrestructure.Models.MySQLPisosModel import MySQLPisosModel
from src.Database.MySQL import Base


class MySQLQuirofanos(Base):
    __tablename__ = 'quirofanos'
    uuid = Column(String(36), primary_key=True)
    number = Column(Integer, nullable=False)
    description = Column(String(255), nullable=False)
    floor_uuid = Column(String(36), ForeignKey('floors.uuid'), nullable=False)
    floor = relationship(MySQLPisosModel, backref=backref('quirofanos', uselist=True, cascade="all, delete"))
