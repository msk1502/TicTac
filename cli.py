from logic import Board

_name_ = '_main_'

if _name_ == '_main_':
    BoardTicTac = Board() #makes empty board
    winner = None #sets winner to none
    play = True #play is the condition that continues game if true

    #get player info and assign X and O
    AI_Num = input('How many AI? (0, 1, or 2):')

    if AI_Num == '0' or AI_Num == '1':
        Player1 = input('Player 1 what is your name? ')
        print(Player1, 'you are X')

        if AI_Num == '0':
            Player2 = input('Player 2 what is your name? ')
            print(Player2, 'you are O')

    print('Lets play Tic Tac Toe!')
    print(BoardTicTac.board[0], '\n', BoardTicTac.board[1], '\n', BoardTicTac.board[2]) #prints empty board

    while play == True: #loop continues while play is true
        
        #Goes through players 1 turn and players 2 turn in order during each loop.  Checks if player is AI or not. Checks if anyone won between turns
        if winner == None:
            if AI_Num != '2':
                BoardTicTac.inputMove(Player1, 'X')
                winner = BoardTicTac.get_winner()
            else:
                BoardTicTac.AI_Move('X')
                winner = BoardTicTac.get_winner()   

        if winner == None:
            if AI_Num == '0':
                BoardTicTac.inputMove(Player2, 'O')
                winner = BoardTicTac.get_winner()
            else:
                BoardTicTac.AI_Move('O')
                winner = BoardTicTac.get_winner()

        #output if someone has won
        if winner != None:
            if winner == 'Draw':
                print('Game is a Draw!')
            else:
                print(winner, 'has won!')

            playAgain = input('Do you want to play again?(Y/N): ') #asks players if they want to play again

            #if yes restarts game with empty board 
            if playAgain == 'Y' or playAgain == 'y' or playAgain == 'Yes' or playAgain =='YES' or playAgain == 'yes':
                BoardTicTac.make_empty_board()

                #get player info and assign X and O
                AI_Num = input('How many AI? (0, 1, or 2):')

                if AI_Num == '0' or AI_Num == '1':
                    Player1 = input('Player 1 what is your name? ')
                    print(Player1, 'you are X')

                if AI_Num == '0':
                    Player2 = input('Player 2 what is your name? ')
                    print(Player2, 'you are O')

                winner = None
            #if no ends loop completing program
            elif playAgain == 'N' or playAgain == 'n' or playAgain == 'No' or playAgain == 'NO' or playAgain == 'no':
                play = False
                print('Thanks for playing!')
