import unittest
from flask import Flask
from flask_testing import TestCase
from unittest.mock import patch
from src.CloudHealt.Infrestructure.Routes import PacientesRoutes


class TestUserRoutes(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.register_blueprint(PacientesRoutes.pacientes_routes, url_prefix="/pacientes")
        return app

    def test_paciente_exists(self):
        response = self.client.get('/pacientes/defb1abc-7aa3-49d7-b4aa-d71e31204941')
        self.assertEqual(response.status_code, 200)
        data_complete = response.get_json()
        data = data_complete['paciente']
        self.assertEqual(data['firstname'], "Juan")
        self.assertEqual(data['lastname'], "Perez Pacheco")

    def test_ubicacion_paciente(self):
        response = self.client.get('/pacientes/bbb44936-1e26-44c4-81a1-7ff73305df1e')
        self.assertEqual(response.status_code, 200)
        data_complete = response.get_json()
        data = data_complete['paciente']
        self.assertEqual(data['cama'], 2)
        self.assertEqual(data['pabellon'], "Cardiologia")
        self.assertEqual(data['piso pabellon'], "Nivel 1")
        self.assertEqual(data['habitacion'], 35)
        self.assertEqual(data['quirofano'], None)
        self.assertEqual(data['piso quirofano'], None)

    def test_stress(self):
        for i in range(100):
            self.test_paciente_exists()

    def test_paciente_not_exists(self):
        response = self.client.get('/pacientes/9e26db42-7c45-4cd5-b047-d35ad3d55e7b')
        self.assertEqual(response.status_code, 404)

    def test_paciente_not_exist_message(self):
        response = self.client.get('/pacientes/9e26db42-7c45-4cd5-b047-d35ad3d55e7b')
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertEqual(data['message'], "Paciente not found")


if __name__ == '__main__':
    unittest.main()
