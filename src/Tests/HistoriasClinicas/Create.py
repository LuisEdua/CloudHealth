import unittest
from flask import Flask, json
from src.CloudHealt.Infrestructure.Routes.HistoriasRoutes import historias_routes
from flask_testing import TestCase


class CreateTest(TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(historias_routes, url_prefix='/historias')
        self.client = self.app.test_client()

    def test_create_historia_success(self):
        historia_data = {"profesion": "Ingeniero", "weight": 70, "high": 175}
        response = self.client.post('/historias/', json=historia_data)
        self.assertEqual(response.status_code, 201)

    def test_create_historia_failure(self):
        historia_data = {"profesion": "Ingeniero", "weight": "incorrect", "high": "incorrect"}
        response = self.client.post('/historias/', json=historia_data)
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
