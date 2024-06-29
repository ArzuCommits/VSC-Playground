class HCF:
    l=int(input("Enter a number to declare the total number of number you want too find the hcf off: "))
    ar=[]
    for i in range (0,l):
        print('Enter number',(i+1),end=": ")
        n=int(input())
        ar.append(n)
    maxx = int(max(ar))
    print('Number listed:',ar[0:])
    c,hcf=2,1
    while c <= maxx:
        count = 0 
        for i in range(0,l):
            if (ar[i] % c == 0):
                count+=1
        if (count == l):
            hcf=c
            c+=1
        else:
            c+=1
    print("\nHCF= ",hcf)