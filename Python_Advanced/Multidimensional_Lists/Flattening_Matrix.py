n = int(input())
numbers = []

for i in range(n):
    data = [int(el) for el in input().split(', ')]
    numbers.extend(data)
print(numbers)

