import logic

Board1 = logic.Board()

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
def test_make_empty_board(board):

        board.make_empty_board()
        assert board.board == boardEmpty, 'did not make empty board'
        print('test_make_empty_board success')

# #tests whether get_winner works
def test_get_winner(Board, XorY):
        boardYVert
        assert Board.get_winner() == XorY, 'Did not return correct winner'
        print('test_get_winner success')

# #tests whether inputMove works    
def test_inputMove(Board, expectedBoard, Player, XorO):
        Board.inputMove(Player, XorO)
        assert  Board.board == expectedBoard, 'Returned board not expected' 
        print('test_inputMove success')

# #test whether AI_Move works
def test_AI_Move(Board, expectedBoard, XorO):
        Board.AI_Move(XorO) 
        assert Board.board == expectedBoard, 'Returned board not expected' 
        print('test_AI_Move success')

_name_='_main_'

if _name_ == '_main_':
        test_make_empty_board(Board1)
        
        Board1.board = boardYVert
        test_get_winner(Board1, 'Y')

   #board to check if inputMove works against.  Can change board to try different tests
        testExpectedBoard = [
                [None, None, None],
                [None, None, None],
                [None, None, 'Y']
                ]
        Board1.make_empty_board
        test_inputMove(Board1, testExpectedBoard, 'Matt', 'Y')

        #test to see if AI_Move method in Board class works
        testExpectedBoard = [
                [None, None, None],
                ['X', 'X', 'Y'],
                [None, None, None]
                ]
        Board1.board = [
                [None, None, None],
                ['X', 'X', None],
                [None, None, None]
                ]

        test_AI_Move(Board1, testExpectedBoard, 'Y')