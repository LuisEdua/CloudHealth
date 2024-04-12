import unittest
from flask import Flask
from src.CloudHealt.Infrestructure.Routes.DiagnosticoRoutes import DataRoutes

class TestGetDiagnosticos(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(DataRoutes, url_prefix='/diagnosticos')
        self.client = self.app.test_client()

    def test_get_diagnosticos_success(self):
        paciente_uuid = 'valid-uuid'
        response = self.client.get(f'/diagnosticos/{paciente_uuid}')
        self.assertEqual(response.status_code, 200)

    def test_get_diagnosticos_not_found(self):
        paciente_uuid = 'non-existent-uuid'
        response = self.client.get(f'/diagnosticos/{paciente_uuid}')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
