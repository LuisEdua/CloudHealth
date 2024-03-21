import uuid

class Deportes:
    def __init__(self, name, historia):
        self.uuid = uuid.uuid4()
        self.name = name
        self.historia_uuid = historia.uuid
