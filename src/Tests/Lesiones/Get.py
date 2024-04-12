import unittest
from flask import Flask
from flask_testing import TestCase
from src.CloudHealt.Infrestructure.Routes.LesionesRoutes import lesiones_routes

class TestGetLesiones(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.register_blueprint(lesiones_routes, url_prefix='/lesiones')
        return app

    def test_get_lesiones_success(self):
        historia_uuid = 'fc372d26-412a-4a77-8b51-6a217007a985'
        response = self.client.get(f'/lesiones/{historia_uuid}')
        self.assert200(response)

    def test_get_lesiones_not_found(self):
        historia_uuid = 'non-existent-uuid'
        response = self.client.get(f'/lesiones/{historia_uuid}')
        self.assert404(response)

if __name__ == '__main__':
    unittest.main()
