import time
class time:
    t1=int(time.time())
    t = time.strftime("%p")
    if t == 'AM':
        print("Good Morning!")
    else:
        print("Good Afternoon/Evening!")
        
        for i in range(100000000):
            pass
        
    #* e=int(time.time() - t1)       
    #* print(e)