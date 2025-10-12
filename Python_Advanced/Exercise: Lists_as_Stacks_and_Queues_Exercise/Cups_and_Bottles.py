from collections import deque

cups_capacity = deque(map(int, input().split()))
filled_bottles = list(map(int, input().split()))

wasted_water = 0

while cups_capacity and filled_bottles:
    cup = cups_capacity[0]
    bottle = filled_bottles.pop()

    if bottle >= cup:
        wasted_water += bottle - cup
        cups_capacity.popleft()
    else:
        cup -= bottle
        cups_capacity[0] = cup
if not cups_capacity:
    print(f"Bottles: {' '.join(map(str, filled_bottles))}")
else:
    print(f"Cups: {' '.join(map(str, cups_capacity))}")

print(f"Wasted litters of water: {wasted_water}")
