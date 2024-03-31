import uuid


class Horarios:
    def __init__(self, hora, minuto, segundo, inicio, final, tratamiento_uuid):
        self.uuid = uuid.uuid4()
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo
        self.inicio = inicio
        self.final = final
        self.tratamiento_uuid = tratamiento_uuid
