import uuid


class Roles:
    def __init__(self, name):
        self.uuid = uuid.uuid4()
        self.name = name
