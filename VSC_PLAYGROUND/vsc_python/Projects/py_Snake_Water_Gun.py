#* Snake, Water, Gun Game 
#* This program allows the user to play the snake, water, gun game against the computer.

#* The user is prompted to choose either snake, water or gun.
#* The computer then randomly chooses between the three options.

#* The rules are:
#* - Snake drinks water - Snake wins
#* - Water drowns gun - Water wins
#* - Gun shoots snake - Gun wins

#* If the user and computer choose the same option, it is a tie. 

#* The user can play continuously until they decide to quit.
#* At the end, the program displays the number of wins, losses and ties.

import random as rand
score_comp=0
score_user=0
choice=('snake','water','gun')
for i in range (10):
    computer = rand.choice(choice)
    try:
        user = str(input("Enter your choice (snake, water, gun): ")).lower()
    except ValueError:
        print(f"Invalid choice {user}, please enter snake, water or gun")
    if user not in choice:
        print(f"Invalid choice {user}, please enter snake, water or gun")
        continue
    elif user==computer:
        print(f"User choice = {user}\ncomputer choice = {computer}\n\nIt's a tie.")
    elif (user == 'snake' and computer == 'gun') or (user == 'water' and computer == 'snake') or (user == 'gun' and computer == 'water'):
        print(f'User choice = {user}\ncomputer choice = {computer}\n\nComputer wins.\n\n')
        score_comp+=1
    elif (user == 'snake' and computer == 'water') or (user == 'gun' and computer == 'snake') or (user == 'water' and computer == 'gun'):
        print(f'User choice = {user}\ncomputer choice = {computer}\n\nUser wins.\n\n')
        score_user+=1
        
print(f"Score: User - {score_user}\nComputer - {score_comp} "+"\nUser wins the match" if score_user>score_comp else "\nComputer wins the match" if score_comp>score_user else "It's a tie")
        
