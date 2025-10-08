import os

path = os.path.join(os.getcwd(), 'text.txt')
try:
    file = open(path, encoding='utf-8')
    print('File found.')
    print(file.read())
    file.close()
except FileNotFoundError:   
    print('File not found.')

print(path)
