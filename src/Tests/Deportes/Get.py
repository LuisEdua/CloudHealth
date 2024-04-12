import unittest
from flask import Flask, jsonify
from src.CloudHealt.Infrestructure.Routes.DeportesRoutes import deportes_routes

class DeportesTestCase(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(deportes_routes, url_prefix='/deportes')
        self.client = self.app.test_client()

    def test_get_deportes_by_historia(self):
        historia_uuid = '19148ee1-aa5c-467a-b8ed-975b9677d0cf'
        response = self.client.get(f'/deportes/{historia_uuid}')
        self.assertEqual(response.status_code, 200)

    def test_get_deportes_by_invalid_historia(self):
        historia_uuid = 'invalid-uuid-here'
        response = self.client.get(f'/deportes/{historia_uuid}')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
