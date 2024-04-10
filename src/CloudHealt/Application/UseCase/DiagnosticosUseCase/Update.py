from src.CloudHealt.Domain.Ports.DiagnosticoPort import DiagnosticoPort as Port


class Update:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, uuid, data):
        try:
            title = data['title']
            description = data['description']
            return self.repository.update_diagnostico(uuid, title, description)
        except Exception as e:
            return {"Message": f"Error: {e}", "status": "error"}, 500
