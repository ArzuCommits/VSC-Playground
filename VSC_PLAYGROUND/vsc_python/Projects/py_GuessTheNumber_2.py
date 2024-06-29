import random
from itertools import count
import time

class GuessTherNumber_2:
    #* program to build a game which allows you to guess a number between 1 to 100
    tim=int(time.strftime("%H"))
    
    if tim >= 5 and tim < 12:
        print("Good morning user,\n\t\t Welcome to number guessing game.")
        
    elif tim >= 12 and tim < 17:
        print("Good afternon user,\n\t\t Welcome to number guessing game.")
        
    elif tim >= 17 and tim < 5:
        print("Good evening user,\n\t\t Welcome to number guessing game.")
        
    t=int(input("Enter a number to describe the amount of time you need in seconds to guess the actual number: "))
    
    n=int(input("Enter a number to declare the range: "))
    
    a=random.randint(1,n)
    
    start = time.strftime("%H : %M : %S")
   
    for i in count():
        
        if i == 0:
        
           t1=int(time.time())
           
        try:
            
           e=int(time.time() - t1)
           print("Total sec left: ",t-e)
             
           if( t-e <= 0 ):
            print("Times up!!!")
            print("You failed to guess the correct number which is: ",a)
            break
        
           n = int(input("Please enter your guess: "))
           
           if (n > a):
               print(n,"is too big. Try again...")
               
           elif(n < a):
               print(n,"is too short. Try again...")
               
           else :
               print ("Congratulations! You have won.")
               break
               
        except ValueError:
            
            print("Invalid input. Please enter a number.")
            
    end = time.strftime("%H : %M : %S")        
    print("Started the game at:",start,"\nEnded the game at:",end)