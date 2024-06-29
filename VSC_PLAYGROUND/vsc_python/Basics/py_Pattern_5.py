"""

* 
* *
* * *
* * * *
* * * * *
* * * * * * ... n
* * * * *
* * * *
* * *
* *
*

"""
class Pattern_5:
    n=int(input("Enter a number to declare the range of the pattern: "))
    c=str(input("Enter a following char to print along the program: "))
    for i in range(1 , n+1):
        for j in range(1 , i+1):
            print(c, end=" ")
        print()
    
    for i in range (1,n):
        for j in range (1, (n+1)-i):
            print (c, end=" ")
        print()
    