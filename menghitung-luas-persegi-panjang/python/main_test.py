"""
Tested on python 3.9.7
"""

import unittest
from unittest.mock import patch
import io
from main import calculateAreaRectangle

class TeastCalculateAreaRectangle(unittest.TestCase):
    """
    Mocking stdout for assertion output and make custom decorator
    """
    mock_stdout = patch('sys.stdout', new_callable=io.StringIO)

    """
    Should be successfull
    """
    @mock_stdout
    @patch('builtins.input', side_effect=['3','2'])
    def test_is_calculate_with_wide_greater_than_length(self, _, mock_print):
        calculateAreaRectangle()
        self.assertEqual(mock_print.getvalue(), 'Hasil: 6\n')

    """
    Should be successfull
    """
    @mock_stdout
    @patch('builtins.input', side_effect=['2', '4'])
    def test_is_calculate_with_length_greater_than_wide(self, _, mock_print):
        calculateAreaRectangle()
        self.assertEqual(mock_print.getvalue(), 'Hasil: 8\n')
    
    """
    Should raise ValueError when input wide is aplphabet or what else except integer
    """
    @patch('builtins.input', side_effect=['test', '2'])
    def test_is_bad_int_in_wide(self, _):
        with self.assertRaises(ValueError) as cm:
            calculateAreaRectangle()
        self.assertEqual(cm.exception.args[0], 'Bilangan test*2 bukan integer')

    """
    Should raise ValueError when input length is aplphabet or what else except integer
    """
    @patch('builtins.input', side_effect=['4', 'test'])
    def test_is_bad_int_in_length(self, _):
        with self.assertRaises(ValueError) as cm:
            calculateAreaRectangle()
        self.assertEqual(cm.exception.args[0], 'Bilangan 4*test bukan integer')
    
    """
    Should raise ValueError when input wide is empty
    """
    @patch('builtins.input', side_effect=['', '3'])
    def test_is_bad_int_if_wide_is_empty(self, _):
        with self.assertRaises(ValueError) as cm:
            calculateAreaRectangle()
        self.assertEqual(cm.exception.args[0], 'Bilangan *3 bukan integer')

    """
    Should raise ValueError when length wide is empty
    """
    @patch('builtins.input', side_effect=['2', ''])
    def test_is_bad_int_if_length_is_empty(self, _):
        with self.assertRaises(ValueError) as cm:
            calculateAreaRectangle()
        self.assertEqual(cm.exception.args[0], 'Bilangan 2* bukan integer')

    """
    Should raise ValueError when both input is empty
    """
    @patch('builtins.input', side_effect=['', ''])
    def test_is_bad_int_in_both_input_is_empty(self, _):
        with self.assertRaises(ValueError) as cm:
            calculateAreaRectangle()
        self.assertEqual(cm.exception.args[0], 'Bilangan * bukan integer')

if __name__ == '__main__':
    unittest.main(verbosity=2)