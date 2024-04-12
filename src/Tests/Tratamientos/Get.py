import unittest
from flask import Flask
from flask_testing import TestCase
from src.CloudHealt.Infrestructure.Routes.TratamientosRoutes import DataRoutes

class TestGetTratamientos(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.register_blueprint(DataRoutes, url_prefix='/tratamientos')
        return app

    def test_get_tratamientos_success(self):
        paciente_uuid = 'valid-paciente-uuid'
        response = self.client.get(f'/tratamientos/{paciente_uuid}')
        self.assert200(response)
        self.assertIsInstance(response.json, list)

    def test_get_tratamientos_not_found(self):
        paciente_uuid = 'non-existent-paciente-uuid'
        response = self.client.get(f'/tratamientos/{paciente_uuid}')
        self.assert404(response)

if __name__ == '__main__':
    unittest.main()
