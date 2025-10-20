def is_in_range(param, scope):
    return 0 <= param < scope

direction_mapper = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

rows, cols = [int(el) for el in input().split(", ")]
matrix = []
current_position = None
bomb_position = None

for row_index in range(rows):
    row_data = list(input())
    if "C" in row_data:
        current_position = (row_index, row_data.index("C"))
    if "B" in row_data:
        bomb_position = (row_index, row_data.index("B"))
    matrix.append(row_data)

seconds = 16

while True:
    if seconds <= 0:
        print("Terrorists win!")
        print("Bomb was not defused successfully!")
        print(f"Time needed: {abs(seconds)} second/s.")
        break

    direction = input()

    if direction == "defuse":
        if current_position != bomb_position:
            seconds -= 2
            continue
        else:
            if seconds >= 4:
                seconds -= 4
                matrix[current_position[0]][current_position[1]] = "D"
                print("Counter-terrorist wins!")
                print(f"Bomb has been defused: {seconds} second/s remaining.")
                break
            else:
                seconds -= 4
                matrix[current_position[0]][current_position[1]] = "X"
                print("Terrorists win!")
                print("Bomb was not defused successfully!")
                print(f"Time needed: {abs(seconds)} second/s.")
                break

    seconds -= 1
    row_move, col_move = direction_mapper.get(direction, (0, 0))
    next_row = current_position[0] + row_move
    next_col = current_position[1] + col_move

    if not (is_in_range(next_row, rows) and is_in_range(next_col, cols)):
        continue

    current_position = (next_row, next_col)

    if matrix[next_row][next_col] == "T":
        matrix[next_row][next_col] = "*"
        print("Terrorists win!")
        break

for row in matrix:
    print("".join(row))

