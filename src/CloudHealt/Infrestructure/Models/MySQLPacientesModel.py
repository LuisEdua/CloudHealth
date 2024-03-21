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

    def to_json(self):
        return {
            "uuid": self.uuid,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "age": self.age,
            "gender": self.gender,
            "birthday": self.birthday,
            "cama": self.cama.number,
            "habitacion": self.cama.habitacion.number,
            "pabellon": self.cama.habitacion.area.name,
            "quirofano": self.quirofano.number,
            "piso pabellon": self.cama.habitacion.area.floor.level,
            "piso quirofano": self.quirofano.floor.level,
            "historia": self.historia.to_json()
        }
