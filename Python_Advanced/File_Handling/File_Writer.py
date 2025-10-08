import os

path = os.path.join(os.getcwd(), 'writing_file.txt')
with open(path, 'w', encoding='utf-8') as f:
    numbers = [10, 20, 30, 40, 50, 60, 70, 85]
    for number in numbers:
        f.write(str(number) + '\n')
print('Numbers exist.')

with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    numbers = [int(line.strip()) for line in lines]
    total = sum(numbers)
    average = total / len(numbers)
print('Numbers are:', numbers)
print('Total:', total)
print(f'Average:, {average:.2f}')
