import unittest
from flask import Flask, json
from src.CloudHealt.Infrestructure.Routes.HabitacionesRoute import DataRoutes

class TestListByAreaHabitaciones(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(DataRoutes, url_prefix='/habitaciones')
        self.client = self.app.test_client()

    def test_list_by_area_success(self):
        area_id = '9aff8923-0453-4211-809e-b11d72ed1c02'
        response = self.client.get(f'/habitaciones/{area_id}')
        self.assertEqual(response.status_code, 200)

    def test_list_by_area_not_found(self):
        area_id = 'non-existent-area'
        response = self.client.get(f'/habitaciones/{area_id}')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
