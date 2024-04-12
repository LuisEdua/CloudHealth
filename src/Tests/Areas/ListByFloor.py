import unittest
from flask import Flask
from flask_testing import TestCase
from src.CloudHealt.Infrestructure.Routes import AreasRoute


class TestListByFloor(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.register_blueprint(AreasRoute.DataRoutes, url_prefix="/areas")
        return app

    def test_list_by_floor(self):
        response = self.client.get("/areas/piso/220c8254-7ba0-459d-b966-e96ff164b3f9")

        self.assertEqual(response.status_code, 200)
        data_complete = response.get_json()
        self.assertEqual(data_complete["status"], "Success")

    def test_list_by_floor_empty(self):
        response = self.client.get("/areas/piso/")
        self.assertEqual(response.status_code, 404)


    def test_list_by_floor_invalid(self):
        response = self.client.get("/areas/piso/220c8254-7ba0-459d-b966-e96ff164b3f")

        self.assertEqual(response.status_code, 404)
        data_complete = response.get_json()
        self.assertEqual(data_complete["status"], "not found")


    def test_stress(self):
        for i in range(100):
            self.test_list_by_floor()



if __name__ == '__main__':
    unittest.main()

