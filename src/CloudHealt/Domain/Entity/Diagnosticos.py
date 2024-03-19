import uuid


class Diagnostico:
    def __init__(self, title, decription, paciente):
        self.uuid = uuid.uuid4()
        self.title = title
        self.decription = decription
        self.paciente_uuid = paciente.uuid
