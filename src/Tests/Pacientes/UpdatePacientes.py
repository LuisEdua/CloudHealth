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

    def test_access_to_info(self):
        response = self.client.put("/pacientes/f47ac10b-58cc-4372-a567-0e02b2c3d479",
                                   json={
                                           "cama": None,
                                           "status": None,
                                           "quirofano": None


                                   })
        self.assertEqual(response.status_code, 200)

        data = response.get_json()['paciente']
        self.assertEqual(data['firstname'], "Luis")
        self.assertEqual(data['lastname'], "Farrera")

    def test_update_data(self):
        response = self.client.put("/pacientes/f47ac10b-58cc-4372-a567-0e02b2c3d479",
                                   json={
                                           "cama": "e2b2a5fa-ebfb-4c9c-a749-80985d25dbf6",
                                           "status": "En reposo",
                                           "quirofano": None
                                   })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()['paciente']
        self.assertEqual(data['cama'], 102)
        self.assertEqual(data['status'], "En reposo")
        self.assertEqual(data['quirofano'], 102)


    def test_update_all_data(self):
        response = self.client.put("/pacientes/f47ac10b-58cc-4372-a567-0e02b2c3d479",
                                   json={
                                       "cama": "b8d1a5d7-67c7-4727-9c15-155b27c5b986",
                                       "status": "En observacion",
                                       "quirofano": "6ba7b810-9dad-11d1-80b4-00c04fd430c8"
                                   })

        self.assertEqual(response.status_code, 200)
        data = response.get_json()['paciente']
        self.assertEqual(data['cama'], 101)
        self.assertEqual(data['status'], "En observacion")
        self.assertEqual(data['quirofano'], 102)

    def test_user_does_not_exist(self):
        response = self.client.put("/pacientes/f47ac10b-58cc-4372-a567-0e02b2c3d477",
                                   json={
                                       "cama": "b8d1a5d7-67c7-4727-9c15-155b27c5b986",
                                       "status": "En observacion",
                                       "quirofano": "6ba7b810-9dad-11d1-80b4-00c04fd430c8"
                                   })
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertEqual(data['status'], "not found")
        self.assertEqual(data['message'], "Paciente not found")


if __name__ == '__main__':
    unittest.main()
