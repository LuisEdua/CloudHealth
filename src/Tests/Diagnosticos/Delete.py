import unittest
from flask import Flask
from src.CloudHealt.Infrestructure.Routes.DiagnosticoRoutes import DataRoutes

class TestDeleteDiagnostico(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(DataRoutes, url_prefix='/diagnosticos')
        self.client = self.app.test_client()

    def test_delete_diagnostico_success(self):
        uuid = 'valid-uuid'
        response = self.client.delete(f'/diagnosticos/{uuid}')
        self.assertEqual(response.status_code, 200)

    def test_delete_diagnostico_not_found(self):
        uuid = 'non-existent-uuid'
        response = self.client.delete(f'/diagnosticos/{uuid}')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
