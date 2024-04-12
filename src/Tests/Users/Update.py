import unittest
from flask import Flask, json
from flask_testing import TestCase
from src.CloudHealt.Infrestructure.Routes.UsuariosRoute import DataRoutes

class TestUpdateUser(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.register_blueprint(DataRoutes, url_prefix='/users')
        return app

    def test_update_user_success(self):
        uuid = 'valid-user-uuid'
        update_data = {
            "email": "updated.email@example.com",
            "password": "newpassword123",
            "area_uuid": "new-area-uuid"
        }
        response = self.client.put(f'/users/{uuid}', json=update_data)
        self.assert200(response)

    def test_update_user_failure(self):
        uuid = 'non-existent-user-uuid'
        update_data = {
            "email": "no.such.user@example.com",
            "password": "doesntmatter",
            "area_uuid": "irrelevant"
        }
        response = self.client.put(f'/users/{uuid}', json=update_data)
        self.assert404(response)  # No user found with the given UUID

if __name__ == '__main__':
    unittest.main()
