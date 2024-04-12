import unittest
from flask import Flask, json
from flask_testing import TestCase
from src.CloudHealt.Infrestructure.Routes.UsuariosRoute import DataRoutes

class TestLoginUser(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.register_blueprint(DataRoutes, url_prefix='/users')
        return app

    def test_login_user_success(self):
        credentials = {"email": "john.doe@example.com", "password": "password123"}
        response = self.client.post('/users/login', json=credentials)
        self.assert200(response)

    def test_login_user_failure(self):
        credentials = {"email": "john.doe@example.com", "password": "wrongpassword"}
        response = self.client.post('/users/login', json=credentials)
        self.assert401(response)  # Assuming 401 Unauthorized for wrong credentials

if __name__ == '__main__':
    unittest.main()
