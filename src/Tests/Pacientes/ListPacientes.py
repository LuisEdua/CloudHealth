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
        response = self.client.get('/pacientes/area/9aff8923-0453-4211-809e-b11d72ed1c02')
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertEqual(data['status'], "Success")

    def test_stress(self):
        for i in range(100):
            self.test_pacientes_list()

    def test_area_not_found(self):
        response = self.client.get('/pacientes/area/291')
        self.assertEqual(response.status_code, 404)

        data = response.get_json()
        self.assertEqual(data['status'], "not found")



if __name__ == '__main__':
    unittest.main()
