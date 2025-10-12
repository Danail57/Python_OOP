n = int(input())
query_stack = []

for _ in range(n):
    query = input().split()

    if query[0] == '1':
        number = int(query[1])
        query_stack.append(number)

    elif query[0] == '2':
        if query_stack:
            query_stack.pop()

    elif query[0] == '3':
        if query_stack:
            print(max(query_stack))

    elif query[0] == '4':
        if query_stack:
            print(min(query_stack))
print(", ".join(map(str, reversed(query_stack))))
