import pywhatkit
import time

hour = int(time.strftime('%H'))
mins = int(time.strftime('%M')) + 2
pywhatkit.sendwhatmsg('+918016801680', 'MESSAGE SENT succcessfully.', hour, mins, 60)

# while True:
#     hour2 = int(time.strftime('%H'))
#     if hour2 - hour == 30:
#         pywhatkit.sendwhatmsg('+916290381114', 'End', hour, mins, 100)
#         break
#     time.sleep(300)