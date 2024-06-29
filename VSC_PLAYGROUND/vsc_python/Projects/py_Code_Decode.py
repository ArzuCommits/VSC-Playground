
#* Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language//

#* Coding://
#* if the word contains atleast 3 characters, remove the first letter and append it at the end//
#*   now append three random characters at the starting and the end//
#* else://
#*   simply reverse the string//

#* Decoding://
#* if the word contains less than 3 characters, reverse it//
#* else://
#*   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning//
import random as rand
import string as st

state = input('enter a statement: ')

#* encodes the given message//
#* This function encodes a message//
def encode(msg):
  #* Initialize an empty string to store the encoded word//
  word = ''
  
  #* Store the original message//
  w = msg
        
  #* Check if the message is at least 3 characters//         
  if len(msg) >= 3:
          
    #* Loop through the first 3 characters//
    for i in range(3):
      #* Add a random letter for each of the first 3 characters//
      word += rand.choice(st.ascii_letters)
            
    #* Shift the first letter to the end of the word//
    #* This shifts the first letter to the end//
    word += w[1:] + w[0]
          
    #* Add 3 random letters to the end//
    #* This loop adds 3 random letters//
    for j in range(3):
      word += rand.choice(st.ascii_letters)
        
  #* If message is less than 3 characters//
  else:
    #* Shift the first letter to the end//
    word += msg[1:] + msg[0]

  #* Print the encoded message//
  print("Encoded message: ", word)


#* decodes encoded message//
def decode(msg):
  
  word = ''
  
  if len(msg) > 3:
      
   #* takes last letter and puts at beginning//
    word = msg[-4:-3] + msg[3:-4]

  else:
      
   #* reverses string if less than 3 letters//
    word = msg[::-1]

  print("Decoded message: ", word)


try:
  
  choice = str(input("Enter 'e' to encode or 'd' to decode: "))
  
  if choice == 'e':
    encode(state)
      
  elif choice == 'd':
    decode(state)
    
except ValueError:
  print("Invalid input")
