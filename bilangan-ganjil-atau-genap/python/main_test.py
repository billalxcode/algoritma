"""
Tested on python 3.9.7
"""

import unittest
from unittest.mock import patch
from main import isEvenOrOdd

class TestIsEvenOrOdd(unittest.TestCase):

    """
    Should be successful with even results
    """
    @patch('builtins.input', return_value=6)
    def test_is_even(self, mock_input):
        self.assertTrue(mock_input() == 6)
        self.assertEqual(isEvenOrOdd(), 0)
    
    """
    Should be successful with odd results
    """
    @patch('builtins.input', return_value=5)
    def test_is_odd(self, mock_input):
        self.assertTrue(mock_input() == 5)
        self.assertEqual(isEvenOrOdd(), 1)

    """
    Should raise ValueError when input with string
    """
    @patch('builtins.input', return_value='test')
    def test_is_bad_int_with_string(self, mock_input):
        self.assertTrue(mock_input() == 'test')
        self.assertRaises(ValueError, isEvenOrOdd)

    """
    Should raise TypeError when input with None
    """
    @patch('builtins.input', return_value=None)
    def test_is_bad_int_with_float(self, mock_input):
        self.assertRaises(TypeError, isEvenOrOdd)
    
    """
    Should be successful with odd results
    when input with float is even
    """
    @patch('builtins.input', return_value=5.6)
    def test_is_odd_with_float_1(self, mock_input):
        self.assertTrue(mock_input(), 5.6)
        self.assertEqual(isEvenOrOdd(), 1)
    
    """
    Should be successful with odd results
    when input with float is odd
    """
    @patch('builtins.input', return_value=5.7)
    def test_is_odd_with_float_2(self, mock_input):
        self.assertTrue(mock_input(), 5.7)
        self.assertEqual(isEvenOrOdd(), 1)
    
    """
    Should be successful with even results
    when input with float is odd
    """
    @patch('builtins.input', return_value=6.1)
    def test_is_even_with_float_1(self, mock_input):
        self.assertTrue(mock_input(), 6.1)
        self.assertEqual(isEvenOrOdd(), 0)
    
    """
    Should be successful with even results
    when input with float is even
    """
    @patch('builtins.input', return_value=6.2)
    def test_is_even_with_float_2(self, mock_input):
        self.assertTrue(mock_input(), 6.2)
        self.assertEqual(isEvenOrOdd(), 0)
    
    """
    Should raise TypeError when input with None
    """
    @patch('builtins.input', return_value=None)
    def test_is_none_with_error(self, mock_input):
        self.assertIsNone(mock_input())
        self.assertRaises(TypeError, isEvenOrOdd)
    
    """
    Should be successful with odd results
    when input with boolean True
    """
    @patch('builtins.input', return_value=True)
    def test_is_odd_with_boolean_true(self, mock_input):
        self.assertTrue(mock_input(), True)
        self.assertEqual(isEvenOrOdd(), 1)
    
    """
    Should be successful with even results
    when input with boolean False
    """
    @patch('builtins.input', return_value=False)
    def test_is_even_with_boolean_false(self, mock_input):
        self.assertFalse(mock_input(), False)
        self.assertEqual(isEvenOrOdd(), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)