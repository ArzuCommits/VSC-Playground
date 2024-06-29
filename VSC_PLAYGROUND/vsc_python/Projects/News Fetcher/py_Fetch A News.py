
import requests
import random 
from datetime import datetime
from deep_translator import GoogleTranslator
from langdetect import detect

choicee = str(input('Want to search new according to the country or personal query: '))
api = '26b83c9940194468a0ef156b7fb7fd28'
user_choic = str(input('If you want to get any single headline then press 1 else press 2: '))
date = str(datetime.now().date())[0:8]

def translation_of_text(sentence):
    translator = GoogleTranslator(source= 'auto', target= 'en')
    translation = translator.translate(sentence)
    return translation

if choicee == 'country':
    
    category = str(input('Enter your desired category: ')).lower()

    while True:
        
        country = str(input('Enter your country code: ')).lower()
        
        if len(country) > 2 or len(country) < 2:
            
            print('Invalid input.\nPLease enter a valid country code.')
            continue
        
        else:
            
            break
        
    url = f'https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={api}'

    response = requests.get(url)
    isResponseStatus = True if response.status_code == 200 else False
    
    if user_choic == '1':
        
        if isResponseStatus:
            
            new_response = response.json()
            articles = new_response['articles']
            article = random.choice(articles)
            if(detect(article['title']) == 'en'):
                print(detect(article['title']))
                print(article['title'],'\n')
                print(article['description'])
            else:
                print('Normal text= ', article['title'])
                print(f"\nTranslated text to english")
                print(translation_of_text(article['title']), '\n')
                # print(detect(article['description']))
                # print(translation_of_text(article['description']) if detect(article['description']) != 'en' else article['description'])

        else:
            
            print('News fetching error.')
    
    elif user_choic == '2':
        
        if isResponseStatus:
            
            for article in response.json()['articles']:
                
                print(article['title'],'\n')
                print(article['description'],'\n')
                print('-'*172,'\n')
            
            
elif choicee == 'query':
     
    day = str(datetime.now().date())[8]+str(datetime.now().date())[9]
    day = int(day)
    
    if day == 1:
        
        day = day - 1
        
    else:
        
        day -= 1
    
    date += str(day)
    query = str(input('What type of news you want: '))
    url = f'https://newsapi.org/v2/everything?q={query}&from={date}&to={str(datetime.now().date())}&sortBy=popularity&apiKey={api}'
    response = requests.get(url)
    print('date=',date,'todate=',str(datetime.now().date()))
    isResponseStatus = True if response.status_code == 200 else False
    response = response.json()
    
    if user_choic == '1':
        
        if isResponseStatus:
            
            articles = response['articles']
            article = random.choice(articles)
            print(article['title'],'\n')
            print(article['description'],'\n')

        else:
            
            print('News fetching error.')
    
    elif user_choic == '2':
        
        if isResponseStatus:
            
            for article in response['articles']:
                
                print(article['title'],'\n')
                print(article['description'],'\n')
                print('-'*172,'\n')
        else:
            print('News fetching error.')
else:
    print(f'Invalid choice {choicee}, please try again.')