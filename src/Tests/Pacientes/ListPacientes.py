import unittest
from flask import Flask
from flask_testing import TestCase
from src.CloudHealt.Infrestructure.Routes import PacientesRoutes

class TestUpdatePacientes(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.register_blueprint(PacientesRoutes.pacientes_routes, url_prefix="/pacientes")
        return app

    def test_pacientes_list(self):
        response = self.client.get('/pacientes/area/2910aa72-e5cd-11ee-b867-f0761cdd1aa9')
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertEqual(data['status'], "Success")

    def test_area_not_found(self):
        response = self.client.get('/pacientes/area/2910aa72-e5cd-11ee-b867-f0761cdd1a88')
        self.assertEqual(response.status_code, 404)

        data = response.get_json()
        self.assertEqual(data['status'], "not found")

    def test_area_not_found(self):
        response = self.client.get('/pacientes/area/291')
        self.assertEqual(response.status_code, 500)

        data = response.get_json()
        self.assertEqual(data['status'], "error")



if __name__ == '__main__':
    unittest.main()
