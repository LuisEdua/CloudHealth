import uuid


class Habitaciones:
    def __init__(self, number):
        self.uuid = uuid.uuid4()
        self.number = number
