"""

1 
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6 . . . n
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

"""
class Pattern_5:
    n=int(input("Enter a number to declare the range of the pattern: "))
    for i in range(1 , n+1):
        for j in range(1 , i+1):
            print(j, end=" ")
        print()
    
    for i in range (1,n):
        for j in range (1, (n+1)-i):
            print (j, end=" ")
        print()
    