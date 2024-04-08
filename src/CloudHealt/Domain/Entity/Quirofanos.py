import uuid


class Quirofanos:
    def __init__(self, number, description, floor_uuid):
        self.uuid = uuid.uuid4()
        self.number = number
        self.description = description
        self.floor_uuid = floor_uuid

