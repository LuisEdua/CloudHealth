import unittest
from flask import Flask
from flask_testing import TestCase
from src.CloudHealt.Infrestructure.Routes.UsuariosRoute import DataRoutes

class TestGetAllUsers(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.register_blueprint(DataRoutes, url_prefix='/users')
        return app

    def test_get_all_users(self):
        response = self.client.get('/users/')
        self.assert200(response)

if __name__ == '__main__':
    unittest.main()
