import unittest
from flask import Flask
from flask_testing import TestCase
from src.CloudHealt.Infrestructure.Routes.UsuariosRoute import DataRoutes

class TestGetUsersByArea(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.register_blueprint(DataRoutes, url_prefix='/users')
        return app

    def test_get_users_by_area_success(self):
        area_uuid = 'valid-area-uuid'
        response = self.client.get(f'/users/{area_uuid}')
        self.assert200(response)
        self.assertIsInstance(response.json, list)  # Expecting a list of users

    def test_get_users_by_area_no_users(self):
        area_uuid = 'empty-area-uuid'
        response = self.client.get(f'/users/{area_uuid}')
        self.assert200(response)
        self.assertEqual(response.json, [])  # No users found in the given area

if __name__ == '__main__':
    unittest.main()
