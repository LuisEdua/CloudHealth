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
        pass

    def registerPaciente(self, paciente: Pacientes):
        new = Model(uuid=paciente.uuid, firstname=paciente.firstname, lastname=paciente.lastname,
                    age=paciente.age, gender=paciente.gender, birthday=paciente.birthday,
                    quirofano_uuid=paciente.quirofano_uuid, cama_uuid=paciente.uuid)
        self.db.add(new)
        self.db.commit()
        return new.to_json()

    def updatePaciente(self, status, cama):
        pass
