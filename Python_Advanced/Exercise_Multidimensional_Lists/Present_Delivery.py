presents = int(input())
n = int(input())


matrix = []
santa = []
nice_kids = 0

for row in range(n):
    line = input().split()
    matrix.append(line)
    for col in range(n):
        if matrix[row][col] == 'S':
            santa = [row, col]
        elif line[col] == 'V':
            nice_kids += 1

nice_kids_gifted = 0
directions = {'up': (-1, 0),
                  'down': (1, 0),
                  'left': (0, -1),
                  'right': (0, 1)}

while presents > 0:
    command = input()
    if command == 'Christmas morning':
        break
    next_row = santa[0] + directions[command][0]
    next_col = santa[1] + directions[command][1]

    if 0 <= next_row < n and 0 <= next_col < n:
        if matrix[next_row][next_col] == 'V':
            presents -= 1
            nice_kids_gifted += 1
            matrix[next_row][next_col] = '-'

        elif matrix[next_row][next_col] == 'C':
            for direction in directions:
                next_r = next_row + directions[direction][0]
                next_c = next_col + directions[direction][1]
                if 0 <= next_r < n and 0 <= next_c < n:
                    if matrix[next_r][next_c] in 'VX' and presents > 0:
                        if matrix[next_r][next_c] == 'V':
                            nice_kids_gifted += 1
                        presents -= 1
                        matrix[next_r][next_c] = '-'

        matrix[santa[0]][santa[1]] = '-'
        santa = [next_row, next_col]
        matrix[santa[0]][santa[1]] = 'S'
if presents == 0 and nice_kids_gifted < nice_kids:
    print("Santa ran out of presents!")

for row in matrix:
    print(' '.join(row))
if nice_kids_gifted == nice_kids:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - nice_kids_gifted} nice kid/s.")
