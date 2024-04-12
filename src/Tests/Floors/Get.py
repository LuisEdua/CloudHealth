import unittest
from flask import Flask
from src.CloudHealt.Infrestructure.Routes.FloorRoute import DataRoutes

class TestPisoListar(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(DataRoutes, url_prefix='/pisos')
        self.client = self.app.test_client()

    def test_piso_listar_success(self):
        response = self.client.get('/pisos/')
        self.assertEqual(response.status_code, 200)

    def test_piso_listar_empty(self):
        response = self.client.get('/pisos/')
        self.assertEqual(response.status_code, 200)
if __name__ == '__main__':
    unittest.main()
