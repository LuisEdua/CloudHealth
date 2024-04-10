from src.CloudHealt.Domain.Ports.UsersPort import UsersPort as Port
from src.CloudHealt.Application.UseCase.UsersUseCase.GetAll import GetAll as UseCase


class GetAllController:
    def __init__(self, repository: Port):
        self.use_case = UseCase(repository)

    def run(self):
        return self.use_case.run()
