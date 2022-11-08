# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.

#creates and returns empty board
def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

#checks if there is a winner.  If there is returns X or O depending upon who won.  Returns None if no winner
def get_winner(Board):
    
    Winner = None #The Winner of the game. X, O or None if draw
    Outcome = None #eventual return value

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
    x = int(input('Enter X coordinate: '))
    y = int(input('Enter Y coordinate: '))


    if 0 > x  or x > 2 or  0 > y or y > 2:  
        #checks if it is outside the image's bounds
        print('Outside Board.  Please enter new coordinates between 0 and 2')
        return inputMove(Board, Player, XorO) #returns board
    elif Board[y][x] != None:
        #checks if the selected space does not equal none
        print('Spot already taken.  Please enter new coordinates')
        return inputMove(Board, Player, XorO) #returns board

    #updates a board to player's move
    Board[y][x] = XorO

    #prints current board
    print(Board[0], '\n', Board[1], '\n', Board[2])

    return Board