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

    #check for draw
    draw = False
    flat_Board = [item for row in Board for item in row]
    if flat_Board.count(None) == 0:
        Outcome = 'Draw'

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


#Chooses move for AI player.  Trys to block emminent wins.  If no emminent wins chooses first None.  Returns updated board
def AI_Move(Board, XorO):
   
   #checks who is the opponent
    if XorO == 'X':
        oppon = 'O'
    else:
        oppon = 'X'

    columns = [[] for i in range(4)] #empty list of list to build columns

    #checks if two X or O in a row.  Return updated board with move to block win
    y = 0
    for row in Board:
        if row.count(oppon) == 2 and row.count(None) == 1: #checks if two of O or X
            x = row.index(None)
            Board[y][x] = XorO
            print(Board[0], '\n', Board[1], '\n', Board[2])
            return Board

        #builds columns
        for i in range(len((row))):
            columns[i].append(row[i])
            
        y +=1

    
    #checks if two X or O in a column.  Return updated board with move to block win
    y = 0
    for column in columns:
        if column.count(oppon) == 2 and column.count(None) == 1: #checks if two of O or X
            x = column.index(None)
            Board[x][y] = XorO
            print(Board[0], '\n', Board[1], '\n', Board[2])
            return Board

        y += 1
    
    #builds list of list of diagnols
    Diags = [[Board[0][0], Board[1][1], Board[2][2]], [Board[0][2], Board[1][1], Board[2][0]]]

    #checks if two X or O in a column.  Return updated board with move to block win
    DiagNum = 0
    for Diag in Diags:
        if Diag.count(oppon) == 2 and Diag.count(None) == 1: #checks if two of O or X
            
            #if statements to get coordinates of move
            indexNone = Diag.index(None)
            if indexNone == 1:
                Board[1][1] = XorO
            elif indexNone == 0:
                if DiagNum == 0:
                    Board[0][0] = XorO
                else:
                    Board[0][2] = XorO
            elif indexNone == 2:
                if DiagNum == 0:
                    Board[2][2] = XorO
                else:
                    Board[2][0] = XorO
            print(Board[0], '\n', Board[1], '\n', Board[2])
            return Board

        DiagNum += 1

    #if no emminent win returns coordinates of first unoccupied space
    for x in range(len(Board)):
        for y in range(len(Board)):
            if Board[y][x] == None:
                Board[y][x] = XorO
                print(Board[0], '\n', Board[1], '\n', Board[2])
                return Board
    