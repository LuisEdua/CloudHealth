import unittest
from flask import Flask
from flask_testing import TestCase
from src.CloudHealt.Infrestructure.Routes.TratamientosRoutes import DataRoutes

class TestDeleteTratamiento(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.register_blueprint(DataRoutes, url_prefix='/tratamientos')
        return app

    def test_delete_tratamiento_success(self):
        uuid = 'existing-tratamiento-uuid'
        response = self.client.delete(f'/tratamientos/{uuid}')
        self.assert200(response)

    def test_delete_tratamiento_not_found(self):
        uuid = 'non-existent-tratamiento-uuid'
        response = self.client.delete(f'/tratamientos/{uuid}')
        self.assert404(response)

if __name__ == '__main__':
    unittest.main()
