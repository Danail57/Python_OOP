import os

path = os.path.join(os.getcwd(), 'word_counnt.txt')
with open(path, encoding='utf-8') as f:
    for line in f:
        fruit = line.strip()
        if fruit:
            print(f"{fruit} - {len(fruit)} letters")

