import unittest
from flask import Flask
from flask_testing import TestCase
from src.CloudHealt.Infrestructure.Routes import AreasRoute

class TestCreateArea(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.register_blueprint(AreasRoute.DataRoutes, url_prefix="/areas")
        return app

    def test_create_area_success(self):
        response = self.client.post('/areas/', json={
            "name": "Cardiologia",
            "floor_uuid": "220c8254-7ba0-459d-b966-e96ff164b3f9"
        })

        self.assertEqual(response.status_code, 201)

        area_data = response.json.get('area')  # Accessing the 'area' attribute from the JSON response
        self.assertEqual(area_data['name'], "Cardiologia")

    def test_create_area_with_existing_name(self):
        response = self.client.post('/areas/', json={
            "name": "Cardiologia",
            "floor_uuid": "220c8254-7ba0-459d-b966-e96ff164b3f9"
        })

        self.assertEqual(response.status_code, 201)

        response = self.client.post('/areas/', json={
            "name": "Cardiologia",
            "floor_uuid": "220c8254-7ba0-459d-b966-e96ff164b3f9"
        })

        self.assertEqual(response.status_code, 201)  # Assuming that the name must be unique

    def test_create_area_with_invalid_floor_uuid(self):
        response = self.client.post('/areas/', json={
            "name": "Cardiologia",
            "floor_uuid": "invalid-uuid"
        })

        self.assertEqual(response.status_code, 500)  # Assuming that the floor_uuid must be a valid UUID

    def test_create_area_with_missing_data(self):
        response = self.client.post('/areas/', json={})
        self.assertEqual(response.status_code, 500)  # Assuming that both 'name' and 'floor_uuid' are required

if __name__ == '__main__':
    unittest.main()