import os

path  = 'C:/Users/arzur/Downloads/VSC_PLAYGROUND/vsc_python/Projects/Word counter/Text.txt'
essay = list()

with open(path , 'r') as f:
    essay = f.read().split()
print('Length of the essay is:',len(essay))