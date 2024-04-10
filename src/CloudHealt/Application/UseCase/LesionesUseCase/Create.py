from src.CloudHealt.Domain.Entity.Lesiones import Lesiones
from src.CloudHealt.Domain.Ports.LessionesPort import LessionesPort as Port


class Create:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, datas):
        try:
            data = datas['lesiones']
            historia_uuid = datas['historia_uuid']
            lesiones = []

            for datos in data:
                title = datos['title']
                description = datos['description']
                lesion = Lesiones(title, description, historia_uuid)
                lesiones.append(lesion)

            return self.repository.create_lesiones(lesiones)

        except Exception as e:
            return {"Message": f"Error: {e}", "status": "error"}, 500

