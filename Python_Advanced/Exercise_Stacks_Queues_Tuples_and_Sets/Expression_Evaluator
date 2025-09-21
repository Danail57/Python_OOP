from collections import deque


expression = input().split()
numbers = deque()

operators = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b,
}

for character in expression:
    if character not in "+-*/":
        numbers.append(int(character))
    else:
        while len(numbers) > 1:
            first_num = numbers.popleft()
            second_num = numbers.popleft()
            numbers.appendleft(operators[character](first_num, second_num))
print(numbers[0])

Example Input
6 3 - 2 1 * 5 /

Output
1

Comment
6 - 3 = 3 
3 * 2 * 1 = 6 
6 / 5 = 1
