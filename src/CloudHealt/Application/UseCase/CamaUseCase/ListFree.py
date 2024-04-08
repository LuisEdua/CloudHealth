from src.CloudHealt.Domain.Ports.CamasPort import CamasPort as Port


class ListFree:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, area_uuid):
        try:
            return self.repository.get_free_camas(area_uuid)
        except Exception as e:
            return {"error": str(e), "status": "Unexpected error"}, 500
