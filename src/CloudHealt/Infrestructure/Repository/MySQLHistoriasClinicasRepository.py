from src.CloudHealt.Domain.Entity.HistoriasClinicas import HistoriasClinicas
from src.CloudHealt.Domain.Ports.HistoriaClinicaPort import HistoriaClinicaPort
from src.CloudHealt.Infrestructure.Models.MySQLHistoriasClinicasModel import MySQLHistoriasClinicas as Model
from src.Database.MySQL import Base, engine, session_local


class MySQLHistoriasClinicasRepository(HistoriaClinicaPort):

    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.db = session_local()

    def get_historia(self, paciente_uuid):
        pass

    def create_historia(self, historia: HistoriasClinicas):
        new = Model(uuid=historia.uuid, profesion=historia.profesion, weight=historia.weight, high=historia.high)
        self.db.session.add(new)
        self.db.session.commit()
        return new.to_json()
