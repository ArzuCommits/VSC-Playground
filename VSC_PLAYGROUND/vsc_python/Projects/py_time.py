import time
class time:
    t1=int(time.time())
    t = int(time.strftime("%H"))
    if t >= 00 and t < 12:
        print("Good Morning!")
    elif t >= 12 and t < 17:
        print("Good Afternoon!")
    else:
        print('Good Evening!')
        
    #     for i in range(100000000):
    #         pass
        
    # e=int(time.time() - t1)
    # print(e)