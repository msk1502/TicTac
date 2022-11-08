from logic import make_empty_board
from logic import get_winner
from logic import inputMove

_name_ = '_main_'

if _name_ == '_main_':
    Board = make_empty_board() #makes empty board
    winner = None #sets winner to none
    play = True #play is the condition that continues game if true

    #get player info and assign X and O
    Player1 = input('Player 1 what is your name? ')
    print(Player1, 'you are X')
    Player2 = input('Player 2 what is your name? ')
    print(Player2, 'you are O')

    print('Lets play Tic Tac Toe!')
    print(Board[0], '\n', Board[1], '\n', Board[2]) #prints empty board

    while play == True: #loop continues while play is true
        
        #Goes through players 1 turn and players 2 turn in order during each loop.  Checks if anyone won between turns
        if winner == None:
            Board = inputMove(Board, Player1, 'X')
            winner = get_winner(Board)

        if winner == None:
            Board = inputMove(Board, Player2, 'O')
            winner = get_winner(Board)

        #output if someone has won
        if winner != None:
            print(winner, 'has won!')

            playAgain = input('Do you want to play again?(Y/N): ') #asks players if they want to play again

            #if yes restarts game with empty board 
            if playAgain == 'Y' or playAgain == 'y' or playAgain == 'Yes' or playAgain =='YES' or playAgain == 'yes':
                Board = make_empty_board()
                winner = None
            #if no ends loop completing program
            elif playAgain == 'N' or playAgain == 'n' or playAgain == 'No' or playAgain == 'NO' or playAgain == 'no':
                play = False
                print('Thanks for playing!')
