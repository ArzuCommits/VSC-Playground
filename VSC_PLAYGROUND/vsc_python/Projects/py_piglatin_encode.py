from py_Piglatin_2 import piglatin_translated_word as ptl

sentence=str(input("Enter a sentence to convert it into piglatin sentence: "))
words = sentence.split() 
translated_sentence=""
for word in words:
    print(word)
    translated_sentence+=ptl(word)+' '
print('Piglatin sentence is:',translated_sentence.lower())
