import unittest
from flask import Flask
from src.CloudHealt.Infrestructure.Routes.HistoriasRoutes import historias_routes
from flask_testing import TestCase


class GetTest(TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(historias_routes, url_prefix='/historias')
        self.client = self.app.test_client()

    def test_get_historia_success(self):
        paciente_uuid = 'existing-uuid'
        response = self.client.get(f'/historias/{paciente_uuid}')
        self.assertEqual(response.status_code, 200)

    def test_get_historia_not_found(self):
        paciente_uuid = 'non-existent-uuid'
        response = self.client.get(f'/historias/{paciente_uuid}')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()




