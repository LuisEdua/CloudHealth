import unittest
from flask import Flask
from flask_testing import TestCase
from src.CloudHealt.Infrestructure.Routes.UsuariosRoute import DataRoutes

class TestDeleteUser(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.register_blueprint(DataRoutes, url_prefix='/users')
        return app

    def test_delete_user_success(self):
        uuid = 'valid-user-uuid'
        response = self.client.delete(f'/users/{uuid}')
        self.assert200(response)

    def test_delete_user_not_found(self):
        uuid = 'non-existent-user-uuid'
        response = self.client.delete(f'/users/{uuid}')
        self.assert404(response)

if __name__ == '__main__':
    unittest.main()
