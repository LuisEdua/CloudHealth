import uuid


class Diagnosticos:
    def __init__(self, title, description, paciente_uuid):
        self.uuid = uuid.uuid4()
        self.title = title
        self.description = description
        self.paciente_uuid = paciente_uuid
