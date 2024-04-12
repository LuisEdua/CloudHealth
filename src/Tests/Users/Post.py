import unittest
from flask import Flask, json
from flask_testing import TestCase
from src.CloudHealt.Infrestructure.Routes.UsuariosRoute import DataRoutes

class TestCreateUser(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.register_blueprint(DataRoutes, url_prefix='/users')
        return app

    def test_create_user_success(self):
        user_data = {
            "firstname": "John",
            "lastname": "Doe",
            "email": "john.doe@example.com",
            "password": "password123",
            "rol_uuid": "rol-uuid",
            "area_uuid": "area-uuid",
            "birthday": "1990-01-01",
            "age": 30
        }
        response = self.client.post('/users/', json=user_data)
        self.assert200(response)

    def test_create_user_failure(self):
        user_data = {"firstname": "John"}  # Missing required fields
        response = self.client.post('/users/', json=user_data)
        self.assert400(response)

if __name__ == '__main__':
    unittest.main()
