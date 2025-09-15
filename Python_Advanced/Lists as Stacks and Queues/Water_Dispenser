from collections import deque

litres = int(input())
name = input()

queue = deque()
while name != 'Start':
    queue.append(name)
    name = input()

data = input()
while data != 'End':
    if data.startswith('refill'):
        litres_to_fill = int(data.split()[-1])
        litres += litres_to_fill
    elif data.isdigit():
        name = queue.popleft()
        litres_wanted = int(data)
        if litres_wanted <= litres:
            litres -= litres_wanted
            print(f'{name} got water')
        else:
            print(f'{name} must wait')
    data = input()
print(f'{litres} liters left')
