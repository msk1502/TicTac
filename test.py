import unittest
import logic

#Test Boards
boardEmpty = [
        [None, None, None]
        [None, None, None]
        [None, None, None]
        ]

boardXDiag = [
        ['X', None, '0']
        [None, 'X', None]
        [None, 'O', 'X']
        ]

boardYDiag = [
        ['Y', None, 'X']
        [None, 'Y', None]
        [None, 'X', 'Y']
        ]

boardXHoriz = [
        ['X', 'X', 'X']
        [None, 'Y', None]
        ['Y', None, None]
        ]

boardYHoriz = [
        ['Y', 'Y', 'Y']
        [None, 'X', None]
        ['X', None, None]
        ]

boardXVert = [
        ['X', None, 'Y']
        ['X', 'Y', None]
        ['X', None, None]
        ]

boardYVert = [
        ['Y', None, 'X']
        ['Y', 'X', None]
        ['Y', None, None]
        ]

boardDraw = [
        ['X', 'Y', 'X']
        ['Y', 'Y', 'X']
        ['X', 'X', 'Y']
        ]

class TestLogic(unittest.TestCase):

    def test_get_winner(Board, XorY):

        self.assertEqual(logic.get_winner(Board), XorY)

        #TODO: Test all functions from logic.py
    
    def test_inputMove(Board, expectedBoard, Player, XorO):
        self.assertEqual(logic.inputMove(Board, Player, XorO), expectedBoard)

if _name_ == '_main_':
    unittest.main()


