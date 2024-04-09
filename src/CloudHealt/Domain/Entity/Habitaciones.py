import uuid


class Habitaciones:
    def __init__(self, number, area):
        self.uuid = uuid.uuid4()
        self.number = number
        self.area = area

