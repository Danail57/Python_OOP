n = int(input())
matrix = []

for _ in range(n):
    data = list(input())
    matrix.append(data)

searched_symbol = input()
position = None
is_found = False

for row_index in range(n):
    for col_index in range(n):
        if matrix[row_index][col_index] == searched_symbol:
            position = (row_index, col_index)
            is_found = True
            break
    if is_found:
        break
if position:
    print(position)
else:
    print(f'{searched_symbol} does not occur in the matrix')
