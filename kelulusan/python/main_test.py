"""
Tested on python 3.9.7
"""

import unittest
from unittest.mock import patch
import io
from main import checkIsGraduated


class TestIsGraduatedOrNot(unittest.TestCase):
    """
    Mocking stdout for assertion output and make custom decorator
    """
    mock_stdout = patch('sys.stdout', new_callable=io.StringIO)

    """
    Should be successfull with graduated
    """
    @mock_stdout
    @patch('builtins.input', side_effect=['test', '70'])
    def test_is_not_graduted(self, _, mock_print):
        checkIsGraduated()
        self.assertEqual(mock_print.getvalue(), 'Nama: test\nNilai: 70\nKeterangan: Tidak lulus\n')

    """
    Should be successfull with not graduated
    """
    @mock_stdout
    @patch('builtins.input', side_effect=['testing', '71'])
    def test_is_graduted(self, _, mock_print):
        checkIsGraduated()
        self.assertEqual(mock_print.getvalue(), 'Nama: testing\nNilai: 71\nKeterangan: Lulus\n')
    
    """
    Should raise ValueError when input alphabet or what else except integer
    """
    @patch('builtins.input', side_effect=['test', 'test'])
    def test_is_bad_int_with_alphabet(self, _):
        with self.assertRaises(ValueError) as cm:
            checkIsGraduated()
        self.assertEqual(cm.exception.args[0], ('Bilangan test bukan integer'))

    """
    Should raise ValueError when input float
    """
    @patch('builtins.input', side_effect=['test', '80.5'])
    def test_is_bad_int_with_float(self, _):
        with self.assertRaises(ValueError) as cm:
            checkIsGraduated()
        self.assertEqual(cm.exception.args[0], ('Bilangan 80.5 bukan integer'))
    
if __name__ == '__main__':
    unittest.main(verbosity=2)