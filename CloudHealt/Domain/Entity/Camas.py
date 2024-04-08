import uuid


class Camas:
    def __init__(self, number, habitacion_uuid):
        self.uuid = uuid.uuid4()
        self.number = number
        self.habitacion_uuid = habitacion_uuid
