
def prime(n):
    for i in range(2,n):
        if n%i==0:
            check = False
            break
    else:
        check = True
    return check