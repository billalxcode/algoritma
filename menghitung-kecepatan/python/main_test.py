"""
Tested on python 3.9.7
"""

import unittest
from unittest.mock import patch
import io
from main import calculateSpeed

class TestCalculateSpeed(unittest.TestCase):
    """
    Mocking stdout for assertion output and make custom decorator
    """
    mock_stdout = patch('sys.stdout', new_callable=io.StringIO)

    """
    Should be successfull
    """
    @mock_stdout
    @patch('builtins.input', side_effect=['20', '2'])
    def test_is_calculate_with_distance_greater_than_time(self, _, mock_print):
        calculateSpeed()
        self.assertEqual(mock_print.getvalue(), 'Hasil: 10.0/jam\n')
    
    """
    Should be successfull
    """
    @mock_stdout
    @patch('builtins.input', side_effect=['23', '30'])
    def test_is_calculate_with_time_greater_than_distance(self, _, mock_print):
        calculateSpeed()
        self.assertEqual(mock_print.getvalue(), 'Hasil: 0.7666666666666667/jam\n')

    """
    Should raise ValueError when input distance is alphabet or what else except integer
    """
    @patch('builtins.input', side_effect=['test', '23'])
    def test_is_bad_int_in_distance(self, _):
        with self.assertRaises(ValueError) as cm:
            calculateSpeed()
        self.assertEqual(cm.exception.args[0], 'Bilangan test/23 bukan integer')
    
    """
    Should raise ValueError when input time is alphabet or what else except integer
    """
    @patch('builtins.input', side_effect=['23', 'test'])
    def test_is_bad_int_in_time(self, _):
        with self.assertRaises(ValueError) as cm:
            calculateSpeed()
        self.assertEqual(cm.exception.args[0], 'Bilangan 23/test bukan integer')
    
    """
    Should raise ValueError when both input is alphabet or what else except integer
    """
    @patch('builtins.input', side_effect=['test', 'testing'])
    def test_is_bad_int_in_both_input(self, _):
        with self.assertRaises(ValueError) as cm:
            calculateSpeed()
        self.assertEqual(cm.exception.args[0], 'Bilangan test/testing bukan integer')
    
    """
    Should raise ValueError when input distance is empty
    """
    @patch('builtins.input', side_effect=['', '3'])
    def test_is_bad_int_if_distance_input_is_empty(self, _):
        with self.assertRaises(ValueError) as cm:
            calculateSpeed()
        self.assertEqual(cm.exception.args[0], 'Bilangan /3 bukan integer')

    """
    Should raise ValueError when input time is empty 
    """
    @patch('builtins.input', side_effect=['2', ''])
    def test_is_bad_int_if_time_input_is_empty(self, _):
        with self.assertRaises(ValueError) as cm:
            calculateSpeed()
        self.assertEqual(cm.exception.args[0], 'Bilangan 2/ bukan integer')
    
    """
    Should raise ValueError when both input empty
    """
    @patch('builtins.input', side_effect=['', ''])
    def test_is_bad_int_in_both_input_is_empty(self, _):
        with self.assertRaises(ValueError) as cm:
            calculateSpeed()
        self.assertEqual(cm.exception.args[0], 'Bilangan / bukan integer')

if __name__ == '__main__':
    unittest.main(verbosity=2)