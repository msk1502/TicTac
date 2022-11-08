# from logic import make_empty_board

_name_ = '_main_'

if _name_ == '_main_':
    # board = make_empty_board()
    winner = None

    #get player info and assign X and O
    Player1 = input('Player 1 what is your name? ')
    print(Player1, 'you are X')
    Player2 = input('Player 2 what is your name? ')
    print(Player2, 'you are O')

    while winner == None:

        print('Lets play Tic Tac Toe!')
        # TODO: Show the board to the user.
        # TODO: Input a move from the player.
        # TODO: Update the board.
        # TODO: Update who's turn it is.
        winner = 'X0' #FIXME