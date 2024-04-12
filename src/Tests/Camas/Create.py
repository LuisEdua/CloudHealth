from flask_testing import TestCase
from flask import Flask, json
from src.CloudHealt.Infrestructure.Routes import HabitacionesRoute
import unittest

class TestHabitaciones(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.register_blueprint(HabitacionesRoute.DataRoutes, url_prefix='/habitaciones')
        return app

    def test_post_habitaciones_status(self):
        response = self.client.post('/habitaciones/', data=json.dumps({
            "cantidad": 50,
            "inicio": 1,
            "area": "19148ee1-aa5c-467a-b8ed-975b9677d0cf"
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_post_habitaciones_data(self):
        response = self.client.post('/habitaciones/', data=json.dumps({
        }), content_type='application/json')
        self.assertEqual(response.status_code, 500)

if __name__ == '__main__':
    unittest.main()
