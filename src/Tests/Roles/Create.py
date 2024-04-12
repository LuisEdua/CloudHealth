import unittest
from flask import Flask, json
from flask_testing import TestCase
from src.CloudHealt.Infrestructure.Routes.RolesRoute import DataRoutes

class TestCreateRole(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.register_blueprint(DataRoutes, url_prefix='/roles')
        return app

    def test_create_role_success(self):
        role_data = {"name": "Administrator"}
        response = self.client.post('/roles/', json=role_data)
        self.assert200(response)

    def test_create_role_failure(self):
        role_data = {}  # Missing 'name'
        response = self.client.post('/roles/', json=role_data)
        self.assert400(response)

if __name__ == '__main__':
    unittest.main()
