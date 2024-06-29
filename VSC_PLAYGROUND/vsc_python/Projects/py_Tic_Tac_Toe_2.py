
#* Create a two-player Tic-Tac-Toe game where players take turns placing their marks (X or O) on a 3x3 grid. Implement logic to determine the winner or declare a draw.Create a two-player Tic-Tac-Toe game where players take turns placing their marks (X or O) on a 3x3 grid.
#* Implement logic to determine the winner or declare a draw.
import random as rand #* According to the following boards you have to place your likings into the board:
print("According to the following boards you have to place your likings into the board: \n") #* Print the board layout
graphboard = [
 ['0,0','0,1','0,2'],                #* Initialize the graphboard
 ['1,0','1,1','1,2'],
 ['2,0','2,1','2,2'] 
]

board = [                            #* Initialize the empty board
 ['   ', '   ', '   '],
 ['   ', '   ', '   '],
 ['   ', '   ', '   ']
]
computer_choice = [                  #* Initialize computer's choices
 ['0,0','0,1','0,2'], 
 ['1,0','1,1','1,2'],
 ['2,0','2,1','2,2']
]
while True:                                                                    #* Get user input on opponent
    choice=str(input('You want to play with a user or computer: ')).lower() 
    if choice == 'user' or choice == 'computer':
        break
    else:
        print('Imvalid output, please try again.')

        
if choice == 'user':                                      #* If playing against user get names
    PLAEYER1=str(input("Enter the name of player 1: "))
    PLAEYER2=str(input("Enter the name of player 2: "))
    
    
def updated():                                            #* Print updated boards after each turn
    global graphboard
    print('\n')
    for index, rows in enumerate(graphboard):
        print('|'.join(rows))

        if index < 2:
            print('-' * 10)
    print('\n')
    global board
    for index, rows in enumerate(board):
        print('|'.join(rows))

        if index < 2:
            print('-' * 10)
    print('\n')
    

winning_combinations = [
    [(0, 0), (0, 1), (0, 2)],  #* Top row
    [(1, 0), (1, 1), (1, 2)],  #* Middle row
    [(2, 0), (2, 1), (2, 2)],  #* Bottom row
    [(0, 0), (1, 0), (2, 0)],  #* Left column
    [(0, 1), (1, 1), (2, 1)],  #* Middle column
    [(0, 2), (1, 2), (2, 2)],  #* Right column
    [(0, 0), (1, 1), (2, 2)],  #* Diagonal from top-left to bottom-right
    [(0, 2), (1, 1), (2, 0)]   #* Diagonal from top-right to bottom-left
]


def winners():
    for combinations in winning_combinations:
        code1,code2,code3=combinations
            
        if ((board[code1[0]][code1[1]] == ' X ' and board[code2[0]][code2[1]] == ' X ' and board[code3[0]][code3[1]] == ' X ') or \
            (board[code1[0]][code1[1]] == ' O ' and board[code2[0]][code2[1]] == ' O ' and board[code3[0]][code3[1]] == ' O ')):
            return 'won'
    
    if is_board_full(board):
        return 'draw'
    
    return 'continue'

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == '   ':
                return False
    return True

def NullList(board):
    for choice in board:
        if len(choice) == 0:
            board.remove(choice)
                               
if choice == 'user':
    
    for i in range(1,10):
        
        cheker = True
        
        if i == 1:
            updated()
        alt_player=PLAEYER1 if i % 2 == 1  else PLAEYER2
        player = 1 if i % 2 == 1  else 0
        sign = ' X ' if player == 1 else ' O '
        row = int(input(f"{alt_player}: please enter the row number : "))
        column = int(input(f"{alt_player}: please enter the column number : "))
        
        if row > 2 or row < 0 or column > 2 or column < 0:
            print("Invalid input. Please try again")
            i-=1
            continue 
        
        if board[row][column] == '   ':
            board[row][column] = sign
            graphboard[row][column] = sign
        else:
            
            print("This position is already taken/out of bound.")
            print("Please enter a new position")
            i-=1
            continue
        
        updated()
            
        if winners() == 'won':
            print(f"{alt_player}: wins the game\n")
            cheker = False
            break
            
        elif winners() == 'draw':
            print("The match is draw.\n")
            cheker = False
            break
            
        elif winners() == 'continue':
            continue
            
        if cheker == False:
            break
        
elif choice == 'computer':
    
    PLAEYER1=str(input('Enter your name: '))
    
    for i in range(1,10):
        
        cheker = True
        
        if i == 1:
            updated()
            
        player = 1 if i % 2 == 1  else 0
        alt_player= PLAEYER1 if  i % 2 == 1  else 'computer'
        sign = ' X ' if player == 1 else ' O '
        
        if i % 2 == 1:
            
            row = int(input(f"{PLAEYER1}: please enter the row number : "))
            column = int(input(f"{PLAEYER1}: please enter the column number : "))
            
            if row > 2 or row < 0 or column > 2 or column < 0:
                
                print("Invalid input. Please try again")
                i-=1
                continue 
        
            if board[row][column] == '   ':
                
                board[row][column] = sign
                graphboard[row][column] = sign
                user_choice = f'{row},{column}'
                for choices in computer_choice:
                    if user_choice in choices:
                        choices.remove(user_choice)
                NullList(computer_choice)
                
            else:
            
                print("This position is already taken/out of bound.")
                print("Please enter a new position")
                i-=1
                continue
            
        elif i % 2 == 0:

            comp = rand.choice(rand.choice(computer_choice))
            row = int(comp[0])
            column = int(comp[2])
            board[row][column] = sign
            graphboard[row][column] = sign
            
            for choices in computer_choice:
                
                    if comp in choices:
                        choices.remove(comp)
                        
            NullList(computer_choice)
            
        updated()
        
        if winners() == 'won':
            
            print(f"{alt_player}: wins the game\n")
            cheker = False
            break
            
        elif winners() == 'draw':
            
            print("The match is draw.\n")
            cheker = False
            break
            
        elif winners() == 'continue':
            
            continue
            
        if cheker == False:
            
            break
                                   