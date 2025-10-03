SIZE = 5
matrix = []
my_position = []
targets = 0

for row in range(SIZE):
    matrix.append(input().split())
    for col in range(SIZE):
        if matrix[row][col] == 'A':
            my_position = [row, col]
        elif matrix[row][col] == 'x':
            targets += 1

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

targets_down = []

for _ in range(int(input())):
    command = input().split()
    action = command[0]
    direction = command[1]
    move = directions[direction]

    if action == 'shoot':
        row = my_position[0] + move[0]
        col = my_position[1] + move[1]

        while 0 <= row < SIZE and 0 <= col < SIZE:
            if matrix[row][col] == 'x':
                targets_down.append([row, col])
                matrix[row][col] = '.'
                targets -= 1
                break
            row += move[0]
            col += move[1]

        if targets == 0:
            break

    elif action == 'move':
        steps = int(command[2])
        row = my_position[0] + move[0] * steps
        col = my_position[1] + move[1] * steps

        if 0 <= row < SIZE and 0 <= col < SIZE and matrix[row][col] == '.':
            my_position = [row, col]

if targets == 0:
    print(f"Training completed! All {len(targets_down)} targets hit.")
else:
    print(f"Training not completed! {targets} targets left.")

[print(pos) for pos in targets_down]
