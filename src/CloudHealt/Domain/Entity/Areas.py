import uuid


class Areas:
    def __init__(self, name, floor_uuid):
        self.uuid = uuid.uuid4()
        self.name = name
        self.floor_uuid = floor_uuid
