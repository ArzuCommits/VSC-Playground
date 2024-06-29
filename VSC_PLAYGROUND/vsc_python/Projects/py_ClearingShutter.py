import os
path = 'C:/Users/HP/Desktop/vsc_python/Projects/Clear The Shutter'
files = os.listdir(path)
for i,file in enumerate(files):
    if file.endswith('.png'):
        os.rename(os.path.abspath(file) , os.path.join(path,f'{i}.png'))
# for i, file in enumerate(files):
#     if file.endswith('.png'):
#         old_name = os.path.join(path, file)
#         new_name = os.path.join(path, f'{i}.png')
#         os.rename(old_name, new_name)
