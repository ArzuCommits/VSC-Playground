"""

     0
    101
   21012
  3210123
 432101234
54321012345
"""
class Pattern_3:
    n=int(input("Enter a range for the pattern: "))
    
    for i in range (0 , n+1):
        for s in range (n , i , -1):
            print(end="  ")
        for j in range (i , -1 , -1):
            print(j,end=" ")
        for j in range (1 , i+1):
            print(j,end=" ")
        print()
            
        
        
    
    