import unittest
from flask import Flask
from src.CloudHealt.Infrestructure.Routes.DiagnosticoRoutes import DataRoutes

class TestUpdateDiagnostico(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(DataRoutes, url_prefix='/diagnosticos')
        self.client = self.app.test_client()

    def test_update_diagnostico_success(self):
        uuid = 'valid-uuid'
        response = self.client.put(f'/diagnosticos/{uuid}', json={"title": "Updated Title", "description": "Updated Description"})
        self.assertEqual(response.status_code, 200)

    def test_update_diagnostico_not_found(self):
        uuid = 'non-existent-uuid'
        response = self.client.put(f'/diagnosticos/{uuid}', json={"title": "Updated Title", "description": "Updated Description"})
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
