import unittest
from flask import Flask, json
from src.CloudHealt.Infrestructure.Routes.HabitacionesRoute import DataRoutes

class TestListAllHabitaciones(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(DataRoutes, url_prefix='/habitaciones')
        self.client = self.app.test_client()

    def test_list_all_habitaciones_success(self):
        response = self.client.get('/habitaciones/')
        self.assertEqual(response.status_code, 200)

    def test_list_all_habitaciones_empty(self):
        # Simula una respuesta vacía, como si no hubiera habitaciones
        response = self.client.get('/habitaciones/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])

if __name__ == '__main__':
    unittest.main()
