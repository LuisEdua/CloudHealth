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
        response = self.client.get('/pacientes/9e26db42-7c45-4cd5-b047-d35ad3d55e7a')
        self.assertEqual(response.status_code, 200)
        data_complete = response.get_json()
        data = data_complete['paciente']
        self.assertEqual(data['firstname'], "Luis")
        self.assertEqual(data['lastname'], "Farrera")

    def test_ubicacion_paciente(self):
        response = self.client.get('/pacientes/9e26db42-7c45-4cd5-b047-d35ad3d55e7a')
        self.assertEqual(response.status_code, 200)
        data_complete = response.get_json()
        data = data_complete['paciente']
        self.assertEqual(data['cama'], 102)
        self.assertEqual(data['pabellon'], "urgencias")
        self.assertEqual(data['piso pabellon'], "level 1")
        self.assertEqual(data['habitacion'], 201)
        self.assertEqual(data['quirofano'], None)
        self.assertEqual(data['piso quirofano'], None)

    def test_paciente_not_exists(self):
        response = self.client.get('/pacientes/9e26db42-7c45-4cd5-b047-d35ad3d55e7b')
        self.assertEqual(response.status_code, 404)

    def test_paciente_not_exist_message(self):
        response = self.client.get('/pacientes/9e26db42-7c45-4cd5-b047-d35ad3d55e7b')
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertEqual(data['message'], "Paciente not found")

    def test_system_interruption(self):
        with self.client:
            with patch(
                    'src.CloudHealt.Infrestructure.Controllers.PacientesControllers.FindByIDController') as mock_get_patient_info:
                mock_get_patient_info.side_effect = Exception("System interruption")

                response = self.client.get('/pacientes/9e26db42-7c45-4cd5-b047-d35ad3d55e7a')

                self.assertEqual(response.status_code, 500)

                data = response.get_json()
                self.assertEqual(data['message'], "System interruption")

if __name__ == '__main__':
    unittest.main()
