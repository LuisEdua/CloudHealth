import uuid


class HistoriasClinicas:
    def __init__(self, profession, weight, high):
        self.uuid = uuid.uuid4()
        self.profesion = profession
        self.weight = weight
        self.high = high
