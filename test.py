import unittest
import logic
class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board = [
            ['X', None, '0']
            [None, 'X', None]
            [None, 'O', 'X']
        ]
        self.assertEqual(logic.get_winner(board), 'X')

        #TODO: Test all functions from logic.py

if _name_ == '_main_':
    unittest.main()


