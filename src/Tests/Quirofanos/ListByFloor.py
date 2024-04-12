import unittest
from flask import Flask
from src.CloudHealt.Infrestructure.Routes.QirofanoRoutes import DataRoutes

class TestQuirofanosByFloor(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(DataRoutes, url_prefix='/quirofanos')
        self.client = self.app.test_client()

    def test_quirofanos_by_floor_success(self):
        floor_uuid = 'valid-floor-uuid'
        response = self.client.get(f'/quirofanos/{floor_uuid}')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_quirofanos_by_floor_not_found(self):
        floor_uuid = 'non-existent-floor-uuid'
        response = self.client.get(f'/quirofanos/{floor_uuid}')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
