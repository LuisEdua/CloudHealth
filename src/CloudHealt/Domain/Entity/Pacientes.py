import uuid


class Pacientes:
    def __init__(self, firstname: str, lastname: str, age: int, gender: str, birthday: str, cama_uuid: str, quirofano_uuid: str, historia_uuid: str, status: str):
        self.uuid = uuid.uuid4()
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.birthday = birthday
        self.cama = cama_uuid
        self.quirofano_uuid = quirofano_uuid
        self.historia_uuid = historia_uuid
        self.status = status
