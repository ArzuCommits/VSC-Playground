from deep_translator import GoogleTranslator

def translate_sentence(sentence, dest_language):
    translator = GoogleTranslator(source='auto', target=dest_language)
    translation = translator.translate(sentence)
    return translation

sentence = input("Enter a sentence to translate: ")
dest_language = input("Enter the destination language (e.g. 'fr' for French, 'es' for Spanish, etc.): ")
translated_sentence = translate_sentence(sentence, dest_language)
print("Translation:", translated_sentence)