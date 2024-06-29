"""
12345
1234
123
12
1
"""
class Pattern_2:
    n=int(input("Enter a eange for the pattern: "))
    
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
        