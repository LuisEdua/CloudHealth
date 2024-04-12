import unittest
from flask import Flask, json
from flask_testing import TestCase
from src.CloudHealt.Infrestructure.Routes.TratamientosRoutes import DataRoutes

class TestCreateTratamiento(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.register_blueprint(DataRoutes, url_prefix='/tratamientos')
        return app

    def test_create_tratamiento_success(self):
        tratamiento_data = {
            "title": "Physical Therapy",
            "description": "Therapy for back pain",
            "paciente_uuid": "valid-paciente-uuid"
        }
        response = self.client.post('/tratamientos/', json=tratamiento_data)
        self.assert200(response)

    def test_create_tratamiento_failure(self):
        tratamiento_data = {}  # Missing required fields
        response = self.client.post('/tratamientos/', json=tratamiento_data)
        self.assert400(response)

if __name__ == '__main__':
    unittest.main()
