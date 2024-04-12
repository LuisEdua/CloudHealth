import unittest
from flask import Flask, json
from src.CloudHealt.Infrestructure.Routes.HabitacionesRoute import DataRoutes

class TestCreateHabitaciones(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(DataRoutes, url_prefix='/habitaciones')
        self.client = self.app.test_client()

    def test_create_habitaciones_success(self):
        response = self.client.post('/habitaciones/', json={"inicio": 1, "cantidad": 5, "area": "9aff8923-0453-4211-809e-b11d72ed1c02"})
        self.assertEqual(response.status_code, 201)

    def test_create_habitaciones_failure(self):
        response = self.client.post('/habitaciones/', json={"inicio": "wrong", "cantidad": "wrong", "area": "wrong"})
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
