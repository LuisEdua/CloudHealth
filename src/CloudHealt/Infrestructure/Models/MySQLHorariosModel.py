from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from src.Database.MySQL import Base
from src.CloudHealt.Infrestructure.Models.MySQLPacientesModel import MySQLPacientesModels


class MySQLHorariosModel(Base):
    __tablename__ = ''
