import unittest
from unittest.mock import patch
import requests
import json


class TestDeportesEndpoint(unittest.TestCase):
    @patch('requests.post')
    def test_post_deportes(self, mock_post):
        mock_response = {
            "result": [
                {"name": "Fútbol", "status": "active"},
                {"name": "Baloncesto", "status": "active"},
                {"name": "Natación", "status": "active"}
            ]
        }

        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = mock_response

        data = {
            "deportes": [
                {"name": "Fútbol"},
                {"name": "Baloncesto"},
                {"name": "Natación"},
                {"name": "Tenis"},
                {"name": "Atletismo"}
            ],
            "historia_uuid": "634f6dc3-ec36-469c-84fd-5718b3bf55d1"
        }

        # URL del endpoint
        url = 'http://localhost:5000/deportes'

        response = requests.post(url, headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), mock_response)
        mock_post.assert_called_once_with(url, headers={'Content-Type': 'application/json'}, data=json.dumps(data))


if __name__ == '__main__':
    unittest.main()
