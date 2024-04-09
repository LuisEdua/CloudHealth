from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref
from src.CloudHealt.Infrestructure.Models.MySQLAreasModel import MySQLAreasModel
from src.CloudHealt.Infrestructure.Models.MySQLRolesModel import MySQLRolesModel
from src.Database.MySQL import Base


class MySQLUsersModel(Base):
    __tablename__ = 'users'
    uuid = Column(String(36), primary_key=True)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    birthday = Column(DateTime, nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(255), nullable=False)
    rol_uuid = Column(String(36), ForeignKey('roles.uuid'), nullable=False)
    rol = relationship(MySQLRolesModel, backref=backref('users', uselist=True, cascade="all, delete"))
    area_uuid = Column(String(36), ForeignKey('areas.uuid'), nullable=False)
    area = relationship(MySQLAreasModel, backref=backref('users', uselist=True, cascade="all, delete"))
