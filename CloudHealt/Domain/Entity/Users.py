import uuid


class Users:
    def __init__(self, firstname, lastname, email, password, role_uuid, area_uuid, age, birthday):
        self.uuid = uuid.uuid4()
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.role_uuid = role_uuid
        self.area_uuid = area_uuid
        self.birthday = birthday
        self.age = age
