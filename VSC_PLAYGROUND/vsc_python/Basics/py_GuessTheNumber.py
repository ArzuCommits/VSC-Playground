import random
import sys
class py_GuessTheNos: #program to build a game which allows you to guess a number between 1 to 100
    t=int(input("Enter a number to describe the amount of tries you want: "))
    a=random.randint(1,100)
    for i  in range(0,t):
        
        n= int(input("Please enter your guess: "))
        if (n > a):
            print(n,"is too big than the actual guess. Try again in",t,"tries...")
        elif(n < a):
            print(n,"is too short than the actual guess. Try again in",t,"tries...")
        else :
            print ("Congratulations! You have won.")
            sys.exit()
        t-=1
            
    print("You failed to guess the actual number. That is:",a)
    
        
    