class neon:
    n=int(input('Enter a number '))
    sq,d,s=n*n,0,0
    while sq>0:
        d=sq%10
        s+=d
        sq//=10
    if s==n:
        print(n,'is a neon number.')
    else:
        print(n,'is not a neon number.')