from src.CloudHealt.Domain.Entity.Diagnosticos import Diagnosticos
from src.CloudHealt.Domain.Ports.DiagnosticoPort import DiagnosticoPort as Port


class Create:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, data):
        try:
            title = data['title']
            description = data['description']
            paciente = data['paciente_uuid']
            diagnostico = Diagnosticos(title, description, paciente)
            return self.repository.create_diagnostico(diagnostico)
        except Exception as e:
            return {"Message": f"Error: {e}", "status": "error"}, 500
