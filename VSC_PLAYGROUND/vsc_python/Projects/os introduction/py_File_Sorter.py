import os
import datetime
month_path='os introduction/Months'
months=['january','february','march','april','may','june','july','agust','september','october','november','december']
if not os.path.exists('os introduction'):
    os.mkdir('os introduction')
    
if not os.path.exists('os introduction/Months/january.txt'):
    for i in range(12):
        files=os.path.join(month_path,f'{months[i]}.txt')
        open(files,'w').close()
    
choice = int(input(("Emter '1' to input data and '2' to fetch previous data: " )))
if choice == 1:
    
    while True:
        
        model = str(input("Enter model name (enter done to exit): ")).lower()
        
        if model == 'done':
            break
        
        date = str(input(f"Enter the date (enter date in the format: {datetime.datetime.now().date()}/YYYY-MM-DD): "))
        company_name = str(input('Enter the company name: '))
        quantity = str(input('Enter quantity: '))
        model_category = str(input('Enter model category: '))
        
        d=date.split('-')
        
        if d[1] == '01':
            with open(f'os introduction/Months/{months[0]}.txt','a') as f:
                f.write(f'Date: {date}\nCompany Name: {company_name}\nModel Category: {model_category}\nQuantity: {quantity}\n\n')
                
        elif d[1] == '02':
            with open(f'os introduction/Months/{months[1]}.txt','a') as f:
                f.write(f'Date: {date}\nCompany Name: {company_name}\nModel Category: {model_category}\nQuantity: {quantity}\n\n')
                
        elif d[1] == '03':
            with open(f'os introduction/Months/{months[2]}.txt','a') as f:
                f.write(f'Date: {date}\nCompany Name: {company_name}\nModel Category: {model_category}\nQuantity: {quantity}\n\n')
                
        elif d[1] == '04':
            with open(f'os introduction/Months/{months[3]}.txt','a') as f:
                f.write(f'Date: {date}\nCompany Name: {company_name}\nModel Category: {model_category}\nQuantity: {quantity}\n\n')
                
        elif d[1] == '05':
            with open(f'os introduction/Months/{months[4]}.txt','a') as f:
                f.write(f'Date: {date}\nCompany Name: {company_name}\nModel Category: {model_category}\nQuantity: {quantity}\n\n')
                
        elif d[1] == '06':
            with open(f'os introduction/Months/{months[5]}.txt','a') as f:
                f.write(f'Date: {date}\nCompany Name: {company_name}\nModel Category: {model_category}\nQuantity: {quantity}\n\n')
                
        elif d[1] == '07':
            with open(f'os introduction/Months/{months[6]}.txt','a') as f:
                f.write(f'Date: {date}\nCompany Name: {company_name}\nModel Category: {model_category}\nQuantity: {quantity}\n\n')
                
        elif d[1] == '08':
            with open(f'os introduction/Months/{months[7]}.txt','a') as f:
                f.write(f'Date: {date}\nCompany Name: {company_name}\nModel Category: {model_category}\nQuantity: {quantity}\n\n')
                
        elif d[1] == '09':
            with open(f'os introduction/Months/{months[8]}.txt','a') as f:
                f.write(f'Date: {date}\nCompany Name: {company_name}\nModel Category: {model_category}\nQuantity: {quantity}\n\n')
                
        elif d[1] == '10':
            with open(f'os introduction/Months/{months[9]}.txt','a') as f:
                f.write(f'Date: {date}\nCompany Name: {company_name}\nModel Category: {model_category}\nQuantity: {quantity}\n\n')
                
        elif d[1] == '11':
            with open(f'os introduction/Months/{months[10]}.txt','a') as f:
                f.write(f'Date: {date}\nCompany Name: {company_name}\nModel Category: {model_category}\nQuantity: {quantity}\n\n')
                
        elif d[1] == '12':
            with open(f'os introduction/Months/{months[11]}.txt','a') as f:
                f.write(f'Date: {date}\nCompany Name: {company_name}\nModel Category: {model_category}\nQuantity: {quantity}\n\n')    
                   
elif choice == 2:
    select_mon = str(input('Select a month to fetch data accordingly: ')).lower().strip()
    with open(f'os introduction/Months/{select_mon}.txt') as f:
        print(f.read())
            
    