def is_balanced(expression):
    stack = []
    brackets = {")": "(", "}": "{", "]": "["}

    for symbol in expression:
        if symbol in '({[':
            stack.append(symbol)
        elif symbol in ')}]':
            if not stack:
                return False
            if stack.pop() != brackets[symbol]:
                return False
    return len(stack) == 0

expression = input()
if is_balanced(expression):
    print('Balanced!')
else:
    print('Unbalanced!')
