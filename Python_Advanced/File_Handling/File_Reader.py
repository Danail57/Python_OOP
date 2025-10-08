import os

path = os.path.join(os.getcwd(), 'reading_file')
print("Търсим файл на пътя:", path)

if os.path.exists(path):
    with open(path, 'r', encoding='utf-8') as f:
        print(f.read())
else:
    print("File does not exist!")

