import unittest
from flask import Flask
from flask_testing import TestCase
from src.CloudHealt.Infrestructure.Routes import AreasRoute


class TestListAllAreas(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.register_blueprint(AreasRoute.DataRoutes, url_prefix="/areas")
        return app

    def test_all_areas(self):
        response = self.client.get("/areas/")
        self.assertEqual(response.status_code, 200)
        data_complete = response.get_json()
        self.assertEqual(data_complete["status"], "Success")

    def test_stress_areas(self):
        for i in range(100):
            self.test_all_areas()


if __name__ == '__main__':
    unittest.main()
