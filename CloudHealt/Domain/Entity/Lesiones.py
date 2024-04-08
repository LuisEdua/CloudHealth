import uuid

class Lesiones:
    def __init__(self, title, description, historia_clinica):
        self.uuid = uuid.uuid4()
        self.title = title
        self.description = description
        self.historia_uuid = historia_clinica.uuid
