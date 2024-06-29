class py_Calculator: #program to build a claculator
 
   n=float(input())
   c=str(input())
   while c != "=":
       n1=float(input())
       if c == "+":
           n+=n1
       elif c == "-":
           n-=n1
       elif c == "*":
           n*=n1
       elif c == "/":
           n/=n1
       elif c == "=":
           break
       else:
           print("Invalid input")
           exit()
       c=str(input()) 
   print(n)
   