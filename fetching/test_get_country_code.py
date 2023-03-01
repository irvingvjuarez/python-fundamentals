import unittest
from unittest.mock import MagicMock, patch
from get_country_code import get_country_code

class TestGetCountryCode(unittest.TestCase):
    @patch("requests.get")
    def test_get_country_code(self, mock_requests):
        mock_response = MagicMock()
        mock_response.text = '''
        {
            "name": "Irving",
            "country": [
                {
                    "country_id": "MX",
                    "probability": "0.287"
                },
                {
                    "country_id": "PA",
                    "probability": "0.162"
                }
            ]
        }
        '''

        mock_requests.return_value = mock_response
        country_code = get_country_code("Irving")
        self.assertEqual(country_code, "MX")

if __name__ == "__main__":
    unittest.main()