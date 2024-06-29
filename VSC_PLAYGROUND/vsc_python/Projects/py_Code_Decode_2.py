
#* Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

#* Coding:
#* if the word contains atleast 3 characters, remove the first letter and append it at the end
#*   now append three random characters at the starting and the end
#* else:
#*   simply reverse the string

#* Decoding:
#* if the word contains less than 3 characters, reverse it
#* else:
#*   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

import random as rand
import string as st

coding = True

choice=str(input(f"Enter 'e' to encode or 'd' to decode: ")).lower()

statement=str(input("Enter a statement: "))

coding = True if choice == 'e' else False if choice == 'd' else print(f"Invalid choice {choice}")

coded,decode= '',''

if coding:

    word=statement.split(' ')
    for w in word:
        
        r1 = '' 
        r2 = ''                                      
        
        for i in range(3):
            
            r1+=rand.choice(st.ascii_letters)
            r2+=rand.choice(st.ascii_letters)
        
        if len(w) > 2:
            coded += r1+w[1:]+w[0]+r2+' '
            
        elif len(w) == 2:
            coded += w[1]+w[0]+' '
            
        else:
            coded+=w[:]+' '
            
    print('coded message is: ',coded)
            
else:
    word=statement.split(' ')
    
    for w in word:                                 #* Split statement into words
        
        if len(w) > 3:                             #* Check word length for decoding logic 
            decode+=w[-4:-3]+w[3:-4]+" "           #* Remove 3 random characters from start and end and append first letter to beginning
            
        elif len(w) == 2:                          #* Check for words with 2 characters
            decode+=w[1]+w[0]+' ' 
            
        else:
            decode+=w[:]+' '                       #* Reverse 2 character words and add them back together
            
    print(f'Decoded message is: {decode}')         #* final ouput