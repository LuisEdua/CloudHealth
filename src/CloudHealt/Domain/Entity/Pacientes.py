import uuid


class Pacientes:
    def __init__(self, firstname, lastname, age, gender, birthday, cama, historia_clinica, status):
        self.uuid = uuid.uuid4()
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.birthday = birthday
        self.cama = cama.uuid
        self.historia_uuid = historia_clinica.uuid
        self.status = status.uuid
