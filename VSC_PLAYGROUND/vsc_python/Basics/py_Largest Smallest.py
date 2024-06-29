class py_LarSmal:
    li=[]
    while (True):
    
      n=int(input('Enter elements 1-by-1 (enter 0 to exit) '))
      if(n==0):
          break
      li.append(n)
    max,min = li[0],li[0]
    l=len(li)
    for i in range(1,l):
        
          if (min > li[i]):
             min=li[i]
          elif (max < li[i]) :
             max = li[i]
            
    print('Largest element is',max,"\nSmallest element is",min)
      
    
      