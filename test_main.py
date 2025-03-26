import unittest
from unittest.mock import patch
import main

class TestMain(unittest.TestCase):

    @patch('main.generate_response')
    def test_generate_response(self, mock_generate_response):
        mock_generate_response.return_value = "This is a test response."
        response = main.generate_response("test prompt", [])
        self.assertEqual(response, "This is a test response.")

if __name__ == '__main__':
    unittest.main()