#1
sequence_of_numbers = list(map(int, input().split( )))
target_number = int(input())

for x in range(len(sequence_of_numbers)):
    for y in range(x + 1, len(sequence_of_numbers)):
        if sequence_of_numbers[x] + sequence_of_numbers[y] == target_number:
            print(f'{sequence_of_numbers[x]} + {sequence_of_numbers[y]} = {target_number}')


#2
numbers = list(map(int, input().split()))
target_number = int(input())

targets = set()
values_map = {}

for value in numbers:
    if value in targets:
        print(f"{values_map[value]} + {value} = {target_number}")
    else:
        resulting_number = target_number - value
        targets.add(resulting_number)
        values_map[resulting_number] = value
