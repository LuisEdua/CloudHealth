import unittest
from flask import Flask, jsonify
from src.CloudHealt.Infrestructure.Routes.CamasRoutes import camas_routes


class CamasTestCase(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(camas_routes, url_prefix='/camas')
        self.client = self.app.test_client()

    def test_get_all_camas(self):
        response = self.client.get('/camas/')
        self.assertEqual(response.status_code, 200)

    def test_get_free_camas(self):
        area_uuid = '19148ee1-aa5c-467a-b8ed-975b9677d0cf'
        response = self.client.get(f'/camas/{area_uuid}')
        self.assertEqual(response.status_code, 200)

    def test_get_free_camas_whith_invalid_uuid(self):
        area_uuid = '19148ee1-aa5c-467a-b8ed-975b9677d0c'
        response = self.client.get(f'/camas/{area_uuid}')
        self.assertEqual(response.status_code, 404)

# Ejecución de las pruebas
if __name__ == '__main__':
    unittest.main()
