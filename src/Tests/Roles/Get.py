import unittest
from flask import Flask
from flask_testing import TestCase
from src.CloudHealt.Infrestructure.Routes.RolesRoute import DataRoutes

class TestGetRoles(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.register_blueprint(DataRoutes, url_prefix='/roles')
        return app

    def test_get_roles_success(self):
        response = self.client.get('/roles/')
        self.assert200(response)
        self.assertIsInstance(response.json, list)  # Assuming response is a list of roles

if __name__ == '__main__':
    unittest.main()
