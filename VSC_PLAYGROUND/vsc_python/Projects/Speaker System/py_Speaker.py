import win32com.client
import os

list_of_items = list()
speaker = win32com.client.Dispatch('SAPI.SpVoice')
path = 'C:/Users/arzur/Downloads/VSC_PLAYGROUND/vsc_python/Projects/Speaker System/Text For Speaking.txt'
with open(path , 'r') as f:
    speech = f.read()
speaker.speak(speech)