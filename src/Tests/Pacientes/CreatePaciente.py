import unittest
from flask import Flask
from flask_testing import TestCase
from src.CloudHealt.Infrestructure.Routes import PacientesRoutes, HistoriasRoutes


class TestCreatePaciente(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.register_blueprint(PacientesRoutes.pacientes_routes, url_prefix="/pacientes")
        app.register_blueprint(HistoriasRoutes.historias_routes, url_prefix="/historias")
        return app

    def create_historia_clinica(self):
        response = self.client.post('/historias/', json={
            "profesion": "Ingeniero",
            "weight": 75.9,
            "high": 1.83
        })
        print(response.status_code)
        print(response.json)
        historia = response.json.get('Historia')
        return historia['uuid']

    def test_create_paciente_success(self):

        historia = self.create_historia_clinica()

        response = self.client.post('/pacientes/', json={
            "firstname": "Juan",
            "lastname": "Perez Pacheco",
            "age": 16,
            "gender": "male",
            "birthday": "2003-02-10",
            "cama": None,
            "quirofano": None,
            "status": "internado",
            "historia_uuid": historia
        })

        self.assertEqual(response.status_code, 201)

        paciente_data = response.json.get('paciente')  # Accessing the 'paciente' attribute from the JSON response
        self.assertEqual(paciente_data['firstname'], "Juan")
        self.assertEqual(paciente_data['lastname'], "Perez Pacheco")

    def test_doble_registro(self):
        historia = self.create_historia_clinica()
        response = self.client.post('/pacientes/', json={
            "firstname": "Juan",
            "lastname": "Perez Pacheco",
            "age": 16,
            "gender": "male",
            "birthday": "2003-02-10",
            "cama": None,
            "quirofano": None,
            "status": "internado",
            "historia_uuid": historia
        })

        self.assertEqual(response.status_code, 201)

        paciente_data = response.json.get('paciente')  # Accessing the 'paciente' attribute from the JSON response
        self.assertEqual(paciente_data['firstname'], "Juan")
        self.assertEqual(paciente_data['lastname'], "Perez Pacheco")


        historia = self.create_historia_clinica()
        response = self.client.post('/pacientes/', json={
            "firstname": "Juan",
            "lastname": "Perez Pacheco",
            "age": 16,
            "gender": "male",
            "birthday": "2003-02-10",
            "cama": None,
            "quirofano": None,
            "status": "internado",
            "historia_uuid": historia
        })

        self.assertEqual(response.status_code, 201)

        paciente_data = response.json.get('paciente')  # Accessing the 'paciente' attribute from the JSON response
        self.assertEqual(paciente_data['firstname'], "Juan")
        self.assertEqual(paciente_data['lastname'], "Perez Pacheco")


    def test_caracteres(self):

        historia = self.create_historia_clinica()
        response = self.client.post('/pacientes/', json={
            "firstname": "Ju@n",
            "lastname": "Perez Pacheco",
            "age": 16,
            "gender": "male",
            "birthday": "2003-02-10",
            "cama": None,
            "quirofano": None,
            "status": "internado",
            "historia_uuid": historia
        })

        self.assertEqual(response.status_code, 201)

        paciente_data = response.json.get('paciente')  # Accessing the 'paciente' attribute from the JSON response
        self.assertEqual(paciente_data['firstname'], "Ju@n")
        self.assertEqual(paciente_data['lastname'], "Perez Pacheco")


    def test_void_data(self):
        response = self.client.post('/pacientes/', json={})
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
