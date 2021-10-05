"""
Tested on python 3.9.7
"""

import unittest
from unittest.mock import patch
from main import temperature_conversion

class TestTemperaturConversion(unittest.TestCase):

    """
    Should be successful
    """
    @patch('builtins.input', return_value=70)
    def test_conversion_with_int(self, mock_input):
        self.assertTrue(mock_input() == 70)
        self.assertEqual(temperature_conversion(), (158, 56))
    
    """
    Should raise ValueError when input with String
    """
    @patch('builtins.input', return_value='56.5')
    def test_conversion_with_string(self, mock_input):
        self.assertTrue(mock_input() == '56.5')
        with self.assertRaises(ValueError):
            temperature_conversion()

    """
    Should be successful when input with float
    """
    @patch('builtins.input', return_value=56.5)
    def test_conversion_with_float(self, mock_input):
        self.assertTrue(mock_input() == 56.5)
        self.assertEqual(temperature_conversion(), (132.8, 44.800000000000004))

    """
    Should raise TypeError when input None
    """
    @patch('builtins.input', return_value=None)
    def test_conversion_with_None(self, mock_input):
        self.assertIsNone(mock_input())
        self.assertRaises(TypeError, temperature_conversion)
    
    """
    Should be successful when input with boolean True
    """
    @patch('builtins.input', return_value=True)
    def test_conversion_with_None(self, mock_input):
        self.assertTrue(mock_input())
        self.assertEqual(temperature_conversion(), (33.8, 0.8))
    
    """
    Should be success when input with boolean False
    """
    @patch('builtins.input', return_value=False)
    def test_conversion_with_None(self, mock_input):
        self.assertFalse(mock_input())
        self.assertEqual(temperature_conversion(), (32.0, 0.0))
    

if __name__ == '__main__':
    unittest.main(verbosity=2)