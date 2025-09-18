sequence_of_parentheses = input()
stack = []
parentheses = {'(': ')', '[': ']', '{': '}'}

for character in sequence_of_parentheses:
    if character in parentheses:
        stack.append(character)
    elif character in parentheses.values():
        if not stack:
            print('NO')
            break
        last_opening_parentheses = stack.pop()
        if parentheses[last_opening_parentheses] != character:
            print('NO')
            break
else:
    if stack:
        print('NO')
    else:
        print('YES')
