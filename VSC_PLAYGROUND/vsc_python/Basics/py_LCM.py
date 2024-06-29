class LCM:
    l=int(input("Enter a number to declare the total number of number you want too find the lcm off: "))
    ar=[]
    for i in range (0,l):
        print('Enter number',(i+1),end=": ")
        n=int(input())
        ar.append(n)
    maxx = int(max(ar))
    print('Number listed:',ar[0:])
    c,lcm=2,1
    while c <= maxx:
        count = 0 
        for i in range(0,l):
            if (ar[i] % c == 0):
                count+=1
                ar[i]/=c
        if (count > 0):
            lcm*=c
        else:
            c+=1
        check=True
        for i in range (0,l):
            if (ar[i]!=1):
                check=False
        if(check):
            break
    print("\nLCM= ",lcm)