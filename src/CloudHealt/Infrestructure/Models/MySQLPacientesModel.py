from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship, backref
from src.CloudHealt.Infrestructure.Models.MySQLQuirofanosModel import MySQLQuirofanosModel
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
    cama_uuid = Column(String(36), ForeignKey('camas.uuid'), nullable=True, unique=True)
    cama = relationship(MySQLCamasModel, backref=backref('pacientes', uselist=False))
    historia_uuid = Column(String(36), ForeignKey('historiasclinicas.uuid'), nullable=False)
    historia = relationship(MySQLHistoriasClinicas, backref=backref('pacientes', uselist=True, cascade="all, delete"))

    def to_json(self):
        return {
            "uuid": self.uuid,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "age": self.age,
            "gender": self.gender,
            "birthday": self.birthday,
            "cama": self.cama.number if self.cama_uuid is not None else None,
            "habitacion": self.cama.habitacion.number if self.cama_uuid is not None else None,
            "pabellon": self.cama.habitacion.area.name if self.cama_uuid is not None else None,
            "quirofano": self.quirofano.number if self.quirofano_uuid is not None else None,
            "piso pabellon": self.cama.habitacion.area.floor.level if self.cama_uuid is not None else None,
            "piso quirofano": self.quirofano.floor.level if self.quirofano_uuid is not None else None,
            "historia": self.historia.to_json()
        }
