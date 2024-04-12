from src.CloudHealt.Domain.Ports.PacientesPort import PacientesPort as Port
from src.CloudHealt.Domain.Entity.Pacientes import Pacientes


class Create:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, data):
        try:
            firstname = data['firstname']
            lastname = data['lastname']
            age = data['age']
            gender = data['gender']
            birthday = data['birthday']
            cama = data['cama']
            quirofano = data['quirofano']
            historia_uuid = data['historia_uuid']
            status = data['status']
            paciente = Pacientes(firstname, lastname, age, gender, birthday, cama, quirofano, historia_uuid, status)
            return self.repository.registerPaciente(paciente)
        except Exception as e:
            return {"message": f"Error: {e}", "status": "Failed"}
