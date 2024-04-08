from src.CloudHealt.Domain.Entity.Pacientes import Pacientes
from src.CloudHealt.Domain.Ports.PacientesPort import PacientesPort
from src.Database.MySQL import Base, engine, session_local
from src.CloudHealt.Infrestructure.Models.MySQLPacientesModel import MySQLPacientesModels as Model


class MySQLPacienteRepository(PacientesPort):

    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.db = session_local()

    def get_pacientes(self, area_uuid):
        try:
            pacientes = self.db.query(Model).filter(Model.cama.habitacion.area.uuid == area_uuid).all()
            if pacientes:
                return {"message": "pacientes found", "pacientes": [p.to_json() for p in pacientes],
                        "status": "Success"}, 200
            else:
                return {"message": "pacientes not found", "status": "not found"}, 404
        except Exception as e:
            return {"message": str(e), "status": "error"}, 500

    def get_paciente(self, paciente_uuid):
        pass

    def registerPaciente(self, paciente: Pacientes):
        try:
            new = Model(uuid=paciente.uuid, firstname=paciente.firstname, lastname=paciente.lastname,
                        age=paciente.age, gender=paciente.gender, birthday=paciente.birthday,
                        quirofano_uuid=paciente.quirofano_uuid, cama_uuid=paciente.cama,
                        historia_uuid=paciente.historia_uuid)
            self.db.add(new)
            self.db.commit()
            return {"status": "Created", "message": "Paciente created", "paciente": new.to_json()}
        except Exception as e:
            return {"status": "Failed", "message": str(e)}

    def updatePaciente(self, status, cama):
        pass
