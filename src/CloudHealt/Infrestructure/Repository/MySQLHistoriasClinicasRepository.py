from src.CloudHealt.Domain.Entity.HistoriasClinicas import HistoriasClinicas
from src.CloudHealt.Domain.Ports.HistoriaClinicaPort import HistoriaClinicaPort
from src.CloudHealt.Infrestructure.Models.MySQLHistoriasClinicasModel import MySQLHistoriasClinicas as Model
from src.CloudHealt.Infrestructure.Models.MySQLPacientesModel import MySQLPacientesModels
from src.Database.MySQL import Base, engine, session_local


class MySQLHistoriasClinicasRepository(HistoriaClinicaPort):

    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.db = session_local()

    def get_historia(self, paciente_uuid):
        try:
            paciente = self.db.query(MySQLPacientesModels).filter(MySQLPacientesModels.uuid == paciente_uuid).first()
            if paciente:
                return {"Message": "Historia found successfully", "status": "success",
                        "historia": paciente.historia.to_json()}, 200
            else:
                return {"Message": "Historia not found", "status": "not found"}, 404
        except Exception as e:
            return {"Message": f'Error: {e}', 'status': 'error'}, 500

    def create_historia(self, historia: HistoriasClinicas):
        try:
            new = Model(uuid=historia.uuid, profesion=historia.profesion, weight=historia.weight, high=historia.high)
            self.db.add(new)
            self.db.commit()
            return {"Message": "Historia created successfully", "status": "created",
                    "Historia": new.to_json()}, 201
        except Exception as e:
            return {"Message": f'Error: {e}', 'status': "error"}, 500

