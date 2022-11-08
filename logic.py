# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def get_winner(Board):
    
    Winner = None #The Winner of the game. X, O or None if draw
    Outcome = None

    for i in range(3):
        
        #Check Rows
        if Board[i][0] == Board[i][1] == Board[i][2]: #checks to see if a each entry in a row is the same
            if Winner == None or Winner == Board[i][0]: #checks if both X and O has won.  If so turns error to true
                Winner = Board[i][0] #sets the winner X or O
                Outcome = Winner #creates output
            else:
                Outcome = 'Error' 
        
        #Check Columns
        if Board[0][i] == Board[1][i] == Board[2][i]: #checks to see if a each entry in a column is the same
            if Winner == None or Winner == Board[0][i]:
                Winner = Board[0][i]
                Outcome = Winner
            else:
                Outcome = 'Error'
        
    #Check Diagnols
    if(Board[0][0] == Board[1][1] == Board[2][2] or
    Board[0][2] == Board[1][1] == Board[2][0]): #checks to see if a each entry in the diagnols is the same
        if Winner == None or Winner == Board[1][1]:
            Winner = Board[1][1]
            Outcome = Winner
        else:
            Outcome = 'Error'

    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
    return Outcome

def inputMove(Board, Player, XorO):

    #get player inputs
    print(Player, 'it is your turn!')
    x = input('Enter X coordinate: ')
    y = input('Enter Y coordinate: ')


    if (
        Board[x][y] != None or
        0 > x > len(Board[x]) or 
        0 > y > len(Board)
        ):  #checks if the selected space does not equal none or if it is outside the image's bounds
            print('Invalid Location.  Please enter new coordinates')

            return inputMove(Board, Player, XorO) #returns board

    #turns row string into list, replaces old with new, then replaces that row
    row = list(Board[x])
    row[y] = XorO
    Board[x] = ''.join(row)

    print(Board[0], '\n', Board[1], '\n', Board[2])

    return Board