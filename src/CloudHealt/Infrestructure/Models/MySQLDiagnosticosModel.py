from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from src.Database.MySQL import Base
from src.CloudHealt.Infrestructure.Models.MySQLPacientesModel import MySQLPacientesModels
from uuid import uuid4

class MySQLDiagnosticosModel(Base):
    __tablename__ = 'diagnosticos'
    uuid = Column(String(36), primary_key=True, default=uuid4())
    title = Column(String(50), nullable=False)
    description = Column(String(255), nullable=False)
    paciente_uuid = Column(String(36), ForeignKey('pacientes.uuid'), nullable=False)
    paciente = relationship(MySQLPacientesModels, backref=backref('dianosticos', uselist=True, cascade="all, delete"))
