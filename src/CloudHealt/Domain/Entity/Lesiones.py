import uuid

class Lesiones:
    def __init__(self, title, description, historia_uuid):
        self.uuid = uuid.uuid4()
        self.title = title
        self.description = description
        self.historia_uuid = historia_uuid
