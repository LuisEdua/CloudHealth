from src.CloudHealt.Domain.Ports.UsersPort import UsersPort as Port


class GetByArea:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, area_uuid):
        return self.repository.get_users_by_area(area_uuid)
