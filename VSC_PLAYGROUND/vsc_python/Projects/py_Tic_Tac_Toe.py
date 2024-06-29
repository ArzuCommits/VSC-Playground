
#* Create a two-player Tic-Tac-Toe game where players take turns placing their marks (X or O) on a 3x3 grid. Implement logic to determine the winner or declare a draw.Create a two-player Tic-Tac-Toe game where players take turns placing their marks (X or O) on a 3x3 grid.
#* Implement logic to determine the winner or declare a draw.
import random as rand
print("According to the following boards you have to place your likings into the board: \n")
graphboard,board = [['0,0','0,1','0,2'],
        ['1,0','1,1','1,2'],
        ['2,0','2,1','2,2']],[['   ', '   ', '   '],
            ['   ', '   ', '   '],
            ['   ', '   ', '   ']]
PLAEYER1=str(input("Enter the name of player 1: "))
PLAEYER2=str(input("Enter the name of player 2: "))
def updated():
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
    for combinations in winning_combinations:
        code1,code2,code3=combinations
        if (board[code1[0]][code1[1]] == sign and board[code2[0]][code2[1]] == sign and board[code3[0]][code3[1]] == sign):
            print(f"{alt_player}: wins the game\n")
            cheker = False
            break
        elif i == 9:
            print("The match is draw.\n")
            cheker = False
            break
        else:
            continue
    if cheker == False:
        break
