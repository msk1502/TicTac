# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.

class Board:
    def __init__(self):
        self.board =[
                [None, None, None],
                [None, None, None],
                [None, None, None],
                ]

    def make_empty_board(self):
        #creates and returns empty board
        self.board = [
                [None, None, None],
                [None, None, None],
                [None, None, None],
                ]

    #checks if there is a winner.  If there is returns X or O depending upon who won.  Returns None if no winner
    def get_winner(self):
    
        Winner = None #The Winner of the game. X, O or None if draw
        Outcome = None #eventual return value

        for i in range(3):
        
            #Check Rows
            if self.board[i][0] == self.board[i][1] == self.board[i][2]: #checks to see if a each entry in a row is the same
                if Winner == None or Winner == self.board[i][0]: #checks if both X and O has won.  If so turns error to true
                    Winner = self.board[i][0] #sets the winner X or O
                    Outcome = Winner #creates output
                else:
                    Outcome = 'Error' 
        
            #Check Columns
            if self.board[0][i] == self.board[1][i] == self.board[2][i]: #checks to see if a each entry in a column is the same
                if Winner == None or Winner == self.board[0][i]:
                    Winner = self.board[0][i]
                    Outcome = Winner
                else:
                    Outcome = 'Error'
        
        #Check Diagnols
        if(self.board[0][0] == self.board[1][1] == self.board[2][2] or
        self.board[0][2] == self.board[1][1] == self.board[2][0]): #checks to see if a each entry in the diagnols is the same
            if Winner == None or Winner == self.board[1][1]:
                Winner = self.board[1][1]
                Outcome = Winner
            else:
                Outcome = 'Error'

        #check for draw
        draw = False
        flat_Board = [item for row in self.board for item in row]
        if flat_Board.count(None) == 0:
            Outcome = 'Draw'

        """Determines the winner of the given board.
        Returns 'X', 'O', or None."""
        return Outcome

    def inputMove(self, Player, XorO):

        #get player inputs
        print(Player, 'it is your turn!')
        x = int(input('Enter X coordinate: '))
        y = int(input('Enter Y coordinate: '))


        if 0 > x  or x > 2 or  0 > y or y > 2:  
            #checks if it is outside the image's bounds
            print('Outside Board.  Please enter new coordinates between 0 and 2')
            return self.inputMove(self, Player, XorO) #returns board
        elif self.board[y][x] != None:
            #checks if the selected space does not equal none
            print('Spot already taken.  Please enter new coordinates')
            return self.inputMove(self, Player, XorO) #returns board

        #updates a board to player's move
        self.board[y][x] = XorO

        #prints current board
        print(self.board[0], '\n', self.board[1], '\n', self.board[2])



#Chooses move for AI player.  Trys to block emminent wins.  If no emminent wins chooses first None.  Returns updated board
    def AI_Move(self, XorO):
   
        #checks who is the opponent
        if XorO == 'X':
            oppon = 'O'
        else:
            oppon = 'X'

        columns = [[] for i in range(4)] #empty list of list to build columns

        #checks if two X or O in a row.  Return updated board with move to block win
        y = 0
        for row in self.board:
            if row.count(oppon) == 2 and row.count(None) == 1: #checks if two of O or X
                x = row.index(None)
                self.board[y][x] = XorO
                print(self.board[0], '\n', self.board[1], '\n', self.board[2])
                return

        #builds columns
            for i in range(len((row))):
                columns[i].append(row[i])
            
            y +=1

    
        #checks if two X or O in a column.  Return updated board with move to block win
        y = 0
        for column in columns:
            if column.count(oppon) == 2 and column.count(None) == 1: #checks if two of O or X
                x = column.index(None)
                self.board[x][y] = XorO
                print(self.board[0], '\n', self.board[1], '\n', self.board[2])
                return

            y += 1
    
        #builds list of list of diagnols
        Diags = [[self.board[0][0], self.board[1][1], self.board[2][2]], [self.board[0][2], self.board[1][1], self.board[2][0]]]

        #checks if two X or O in a column.  Return updated board with move to block win
        DiagNum = 0
        for Diag in Diags:
            if Diag.count(oppon) == 2 and Diag.count(None) == 1: #checks if two of O or X
            
                #if statements to get coordinates of move
                indexNone = Diag.index(None)
                if indexNone == 1:
                    self.board[1][1] = XorO
                elif indexNone == 0:
                    if DiagNum == 0:
                        self.board[0][0] = XorO
                    else:
                        self.board[0][2] = XorO
                elif indexNone == 2:
                    if DiagNum == 0:
                        self.board[2][2] = XorO
                    else:
                        self.board[2][0] = XorO
                print(self.board[0], '\n', self.board[1], '\n', self.board[2])
                return

            DiagNum += 1

        #if no emminent win returns coordinates of first unoccupied space
        for x in range(len(self.board)):
            for y in range(len(self.board)):
                if self.board[y][x] == None:
                    self.board[y][x] = XorO
                    print(self.board[0], '\n', self.board[1], '\n', self.board[2])
                    return
    