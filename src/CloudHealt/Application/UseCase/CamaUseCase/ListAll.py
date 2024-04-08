from src.CloudHealt.Domain.Ports.CamasPort import CamasPort as Port


class ListAll:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self):
        try:
            return self.repository.get_all_camas()
        except Exception as e:
            return {"error": str(e), "status": "Unexpected error"}, 500
