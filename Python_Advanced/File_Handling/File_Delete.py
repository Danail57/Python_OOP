import os

path = os.path.join(os.getcwd(), 'delete_file.txt')

if os.path.exists(path):
    os.remove(path)
    print('File successfully deleted.')
else:
    print('File not found.')
