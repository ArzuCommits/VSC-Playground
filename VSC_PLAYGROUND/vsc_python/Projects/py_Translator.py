import translate
from langdetect import detect

text = str(input("Enter a text: "))

translator = translate.Translator(to_lang='en', from_lang='auto')

detection = detect(text)
print(detection)