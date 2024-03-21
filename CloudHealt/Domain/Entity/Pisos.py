import uuid


class Pisos:
    def __init__(self, level):
        self.uuid = uuid.uuid4()
        self.level = level
