import unittest
from flask import Flask, json
from flask_testing import TestCase
from src.CloudHealt.Infrestructure.Routes.LesionesRoutes import lesiones_routes

class TestCreateLesiones(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.register_blueprint(lesiones_routes, url_prefix='/lesiones')
        return app

    def test_create_lesiones_success(self):
        lesiones_data = {
            "lesiones": [
                {"title": "Fractura", "description": "Fractura de brazo"}
            ],
            "historia_uuid": "valid-uuid"
        }
        response = self.client.post('/lesiones/', json=lesiones_data)
        self.assert200(response)

    def test_create_lesiones_failure(self):
        lesiones_data = {}  # Datos incorrectos
        response = self.client.post('/lesiones/', json=lesiones_data)
        self.assert400(response)

if __name__ == '__main__':
    unittest.main()
