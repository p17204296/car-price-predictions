import unittest
from unittest.mock import patch, mock_open

from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder

from backend.ml_model.load_model import regrModel, encoder, cars_csv, newModel


class TestLoadModel(unittest.TestCase):
    @patch('builtins.open',
           mock_open(read_data='mocked_data'))  # Mock the open() function to simulate loading a pickle file
    def test_load_regrModel(self):
        # Ensure that regrModel is an instance of RandomForestRegressor
        self.assertIsInstance(regrModel, RandomForestRegressor)

    def test_load_encoder(self):
        # Ensure that encoder is an instance of OneHotEncoder
        self.assertIsInstance(encoder, OneHotEncoder)

    def test_load_cars_csv(self):
        # Ensure that cars_csv is a valid path to a CSV file
        self.assertIsInstance(cars_csv, str)
        self.assertTrue(cars_csv.endswith('.csv'))

    def test_load_newModel(self):
        # Ensure that newModel is an instance of a loaded model (assuming it's a linear regression model)
        self.assertIsNotNone(newModel)  # Check if newModel is not None


if __name__ == '__main__':
    unittest.main()
