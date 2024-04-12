import unittest
from flask import Flask, json
from src.CloudHealt.Infrestructure.Routes.QuirofanoRoute import DataRoutes

class TestQuirofanoCrear(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(DataRoutes, url_prefix='/quirofanos')
        self.client = self.app.test_client()

    def test_quirofano_crear_success(self):
        quirofano_data = {
            "number": 101,
            "description": "Orthopedic Surgery",
            "floor_uuid": "valid-floor-uuid"
        }
        response = self.client.post('/quirofanos/', json=quirofano_data)
        self.assertEqual(response.status_code, 201)

    def test_quirofano_crear_failure(self):
        quirofano_data = {
            "number": 102
            # Missing 'description' and 'floor_uuid'
        }
        response = self.client.post('/quirofanos/', json=quirofano_data)
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
