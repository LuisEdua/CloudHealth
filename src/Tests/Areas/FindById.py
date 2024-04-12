import unittest
from flask import Flask
from flask_testing import TestCase
from src.CloudHealt.Infrestructure.Routes import AreasRoute


class TestFindById(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.register_blueprint(AreasRoute.DataRoutes, url_prefix="/areas")
        return app


    def test_find_by_id(self):
        response = self.client.get("/areas/2507b106-645f-4df6-b2ab-966c060faedd")
        self.assertEqual(response.status_code, 200)
        data_complete = response.get_json()
        area = data_complete["area"]
        self.assertEqual(area["name"], "Cardiologia")


    def test_find_by_id_not_found(self):
        response = self.client.get("/areas/2507b106-645f-4df6-b2ab-966c060faed")

        self.assertEqual(response.status_code, 404)
        data_complete = response.get_json()
        self.assertEqual(data_complete["status"], "not found")


    def test_stress(self):
        for i in range(100):
            self.test_find_by_id()


if __name__ == '__main__':
    unittest.main()
