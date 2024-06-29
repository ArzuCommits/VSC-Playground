import datetime
import time
import winsound

#* The modified alarm clock project is designed to serve as a reminder system for managing payments by specific dates.
#* Its purpose is to help users keep track of upcoming payments and ensure that they make payments on time. 
#* By allowing users to set payment reminders with associated dates and names, the project provides a convenient way to stay organized and avoid missing payment deadlines. 
#* This enhanced functionality adds a practical aspect to the traditional alarm clock, making it a valuable tool for personal finance management.

payments = {}

while True:
    
    name = input("Enter a name for the alarm (or done to exit): ") #* Ask user for alarm name or 'done' to exit loop
    
    if name.lower() == 'done':
        break
    
    amount = float(input("Enter the amount of the payment: ")) #* Get payment amount from user
    date = str(input(f"Enter the date for the alarm(enter date in the format: {datetime.datetime.now().date()}/YYYY-MM-DD): ")) #* Ask user for payment date in specified format
    
    if date in payments: #* If date already exists in dict
        
        payments[date].append({'name': name, 'amount': amount}) #* Add new payment to existing list
        
    else:
        
        payments[date] = [{'name': name, 'amount': amount}] #* Create new list with payment
        
while True:
    
    current_datetime=str(datetime.datetime.now().date()) #* Get current date
    
    if(current_datetime in payments): #* If current date has payments
        
        for item in payments[current_datetime]: #* Loop through payments on current date
            
            print(f"Alarm for {item['name']} - Rs. {item['amount']}") #* Print alarm message
            
            winsound.Beep(1000,1000) #* Play beep sound
            
            time.sleep(5) #* Delay before next alarm
            
        del  payments[current_datetime] #* Remove payments for current day from dictionary so it doesn't show again tomorrow
        
    elif len(payments) == 0:
        print('terminating the program')
        break
        
    else:
        
        print("No payments today") #* No payments today message
        
        print('else part')
        time.sleep(60) #todo this part needs to be evaluated agian after some evident research
