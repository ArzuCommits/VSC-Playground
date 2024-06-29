""""
Pig Latin is a language game in English in which words are altered according to the rules. It is also known as Igpay Atinlay. The given word encrypted into the same language.

Example: Ingstray, emay, oorflay, etc. are the Pig Latin words
"""
import sys
class Piglatin:
    st=(input("Enter a word to convert it into piglatin word: ")).upper()
    if(isinstance(st, str) == False):
        print("Please consider writing names or any type of word instead of numeric values.")
        sys.exit()
    v=['A', 'E', 'I', 'O', 'U']
    l=len(st)
    for i in range (0,l):
        if st[0] in v:
            piglatin=st+'YAY'
            break
        elif st[i] in v:
            w=st[0:i] 
            piglatin=st[i:]+w+'AY'
            break
        elif i == l-1:
            piglatin=st[l-1]+st[:l-1]+'AY'
            break
        else:
            continue
    print("Piglatin word is:",piglatin)