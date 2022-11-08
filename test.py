import logic

#Test Boards
boardEmpty = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
        ]

boardXDiag = [
        ['X', None, '0'],
        [None, 'X', None],
        [None, 'O', 'X']
        ]

boardYDiag = [
        ['Y', None, 'X'],
        [None, 'Y', None],
        [None, 'X', 'Y']
        ]

boardXHoriz = [
        ['X', 'X', 'X'],
        [None, 'Y', None],
        ['Y', None, None]
        ]

boardYHoriz = [
        ['Y', 'Y', 'Y'],
        [None, 'X', None],
        ['X', None, None]
        ]

boardXVert = [
        ['X', None, 'Y'],
        ['X', 'Y', None],
        ['X', None, None]
        ]

boardYVert = [
        ['Y', None, 'X'],
        ['Y', 'X', None],
        ['Y', None, None]
        ]

boardDraw = [
        ['X', 'Y', 'X'],
        ['Y', 'Y', 'X'],
        ['X', 'X', 'Y']
        ]


#tests whether make_empty_board works
def test_make_empty_board():
    assert logic.make_empty_board() == boardEmpty, 'did not make empty board'
    print('test_make_empty_board success')

#tests whether get_winner works
def test_get_winner(Board, XorY):

    assert logic.get_winner(Board) == XorY, 'Did not return correct winner'
    print('test_get_winner success')

#tests whether inputMove works    
def test_inputMove(Board, expectedBoard, Player, XorO):
        assert logic.inputMove(Board, Player, XorO) == expectedBoard, 'Returned board not expected' 
        print('test_inputMove2 success')

_name_='_main_'

if _name_ == '_main_':
    test_make_empty_board()

    test_get_winner(boardYVert, 'Y')

   #board to check if inputMove works against.  Can change board to try different tests
    testExpectedBoard = [
        [None, None, None],
        [None, None, None],
        [None, None, 'Y']
        ]

    test_inputMove(boardEmpty, testExpectedBoard, 'Matt', 'Y')


