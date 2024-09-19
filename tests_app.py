import unittest
from flask import Flask
from app import app  # Import the Flask app

class TestFlaskApp(unittest.TestCase):

    # Setup method to initialize test client
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Test the home page
    def test_home(self):
        result = self.app.get('/')  # Sends a GET request to the home page
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Prediction:', result.data)  # Check if 'Prediction:' is in the response

    # Test the predict functionality with valid data
    def test_predict_valid(self):
        # Data to mimic form submission (replace these with appropriate feature values)
        valid_data = {
            'feature1': '5.1',
            'feature2': '3.5',
            'feature3': '1.4',
            'feature4': '0.2'
        }

        result = self.app.post('/predict', data=valid_data)
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Prediction:', result.data)  # Check if prediction is returned

    # Test the predict functionality with invalid data
    def test_predict_invalid(self):
        # Invalid data that should trigger the exception block
        invalid_data = {
            'feature1': 'invalid_value',
            'feature2': '3.5',
            'feature3': '1.4',
            'feature4': '0.2'
        }

        result = self.app.post('/predict', data=invalid_data)
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Error:', result.data)  # Ensure the error message is returned

if __name__ == '__main__':
    unittest.main()
