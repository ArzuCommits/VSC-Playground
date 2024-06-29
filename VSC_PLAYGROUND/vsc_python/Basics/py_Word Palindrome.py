#program to check whether the word passed is a palindrome or not
import sys
class WordPalindrome:
    name=str(input("Enter a name: "))
    l=len(name)
    for i in range(0,l):
        
        if(name[i] != name[l-1]):
            print("The given name",name, "is not a Palindrome")
            sys.exit()
           
        l-=1
            
    print("The given name",name, "is a Palindrome")
            
           
    
    