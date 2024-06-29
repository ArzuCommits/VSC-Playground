class py_Piglatin_2:
        
    def piglatin_translated_word(word:str):
        
        con = ''
        vowels = ['a','e','i','o','u']
        for letters in word:
            if letters.lower() in vowels:
                con += letters
            else:
                break
        return con + word[len(con):] + 'ay'
                


