import unittest
from flask import Flask
from src.CloudHealt.Infrestructure.Routes.FloorRoute import DataRoutes

class TestPisoCrear(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(DataRoutes, url_prefix='/pisos')
        self.client = self.app.test_client()

    def test_piso_crear_success(self):
        response = self.client.post('/pisos/', json={"level": 5})
        self.assertEqual(response.status_code, 201)

    def test_piso_crear_failure(self):
        response = self.client.post('/pisos/', json={})
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
