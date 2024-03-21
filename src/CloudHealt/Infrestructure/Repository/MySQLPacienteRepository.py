from src.CloudHealt.Domain.Entity.Pacientes import Pacientes
from src.CloudHealt.Domain.Ports.PacientesPort import PacientesPort
from src.Database.MySQL import Base, engine, session_local
from src.CloudHealt.Infrestructure.Models.MySQLPacientesModel import MySQLPacientesModels as Model


class MySQLPacienteRepository(PacientesPort):
    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.db = session_local()

    def get_pacientes(self, area_uuid):
        pass

    def get_paciente(self, paciente_uuid):
        paciente = self.db.query(Model).filter(Model.uuid == paciente_uuid).first()
        return {'paciente': paciente.to_json(), 'status': 'Success'} if paciente else {'message': 'Paciente not found', 'status': "false"}

    def registerPaciente(self, paciente: Pacientes):
        pass

    def updatePaciente(self, status, cama):
        pass