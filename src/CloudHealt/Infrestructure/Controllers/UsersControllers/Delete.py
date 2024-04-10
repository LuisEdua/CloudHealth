from src.CloudHealt.Domain.Ports.UsersPort import UsersPort as Port
from src.CloudHealt.Application.UseCase.UsersUseCase.Delete import Delete as UseCase


class DeleteController:
    def __init__(self, repository: Port):
        self.use_case = UseCase(repository)

    def run(self, user_uuid):
        return self.use_case.run(user_uuid)
