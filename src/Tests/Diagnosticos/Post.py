import unittest
from flask import Flask
from src.CloudHealt.Infrestructure.Routes.DiagnosticoRoutes import DataRoutes

class TestCreateDiagnostico(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(DataRoutes, url_prefix='/diagnosticos')
        self.client = self.app.test_client()

    def test_create_diagnostico_success(self):
        response = self.client.post('/diagnosticos/', json={"title": "Test Title", "description": "Test Description", "paciente_uuid": "valid-uuid"})
        self.assertEqual(response.status_code, 201)

    def test_create_diagnostico_bad_request(self):
        response = self.client.post('/diagnosticos/', json={})
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
