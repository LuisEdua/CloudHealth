import unittest
from flask import Flask
from src.CloudHealt.Infrestructure.Routes.QuirofanoRoute import DataRoutes

class TestQuirofanosListar(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(DataRoutes, url_prefix='/quirofanos')
        self.client = self.app.test_client()

    def test_quirofanos_listar_success(self):
        response = self.client.get('/quirofanos/')
        self.assertEqual(response.status_code, 200)
        # Assume response should be a list, even if empty
        self.assertIsInstance(response.json, list)

if __name__ == '__main__':
    unittest.main()
