from src.CloudHealt.Application.UseCase.QuirofanosUseCase.ListAll import ListAll as UseCase
from src.CloudHealt.Domain.Ports.QuirofanosPort import QuirofanosPort as Port


class ListAllController:
    def __init__(self, repository: Port):
        self.use_Case = UseCase(repository)

    def run(self):
        return self.use_Case.run()
