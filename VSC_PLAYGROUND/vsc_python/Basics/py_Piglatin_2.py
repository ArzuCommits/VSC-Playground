def piglatin_translator_word(word):
    word=word.upper()
    v=["A", "E", "I", "O", "U", 'A', 'E', 'I', 'O', 'U']
    l=len(word)
    for i in range (l):
        if word[0] in v:
            piglatin=word+'YAY'
            break
        elif word[i] in v:
            w=word[0:i] 
            piglatin=word[i:]+w+'AY'
            break
        elif i == l-1:
            piglatin=word[l-1]+word[:l-1]+'AY'
            break
        else:
            continue
    return piglatin
    
