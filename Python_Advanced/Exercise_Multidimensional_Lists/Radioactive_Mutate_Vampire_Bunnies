def spread_bunnies(mat, bunnies_set):
    new_bunnies = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for bunny_row, bunny_col in bunnies_set:
        for d_row, d_col in directions:
            new_row, new_col = bunny_row + d_row, bunny_col + d_col
            if 0 <= new_row < len(mat) and 0 <= new_col < len(mat[0]):
                new_bunnies.add((new_row, new_col))
                mat[new_row][new_col] = 'B'

    return mat, bunnies_set.union(new_bunnies)


rows, cols = [int(x) for x in input().split()]
matrix = []
bunnies = set()
player_row = player_col = 0

for row in range(rows):
    line = list(input())
    matrix.append(line)
    for col in range(cols):
        if line[col] == 'P':
            player_row, player_col = row, col
        elif line[col] == 'B':
            bunnies.add((row, col))

commands = list(input())

moves = {
    'U': lambda r, c: (r - 1, c),
    'D': lambda r, c: (r + 1, c),
    'L': lambda r, c: (r, c - 1),
    'R': lambda r, c: (r, c + 1),
}

has_won = False
is_dead = False

for command in commands:
    new_row, new_col = moves[command](player_row, player_col)
    matrix[player_row][player_col] = '.' 

    if not (0 <= new_row < rows) or not (0 <= new_col < cols):
        has_won = True
        matrix, bunnies = spread_bunnies(matrix, bunnies)
        break

    if matrix[new_row][new_col] == 'B':
        player_row, player_col = new_row, new_col
        matrix, bunnies = spread_bunnies(matrix, bunnies)
        is_dead = True
        break

    matrix[new_row][new_col] = 'P'
    player_row, player_col = new_row, new_col

    # Зайците се разпространяват
    matrix, bunnies = spread_bunnies(matrix, bunnies)

    if (player_row, player_col) in bunnies:
        is_dead = True
        break

for row in matrix:
    print(''.join(row))


if has_won:
    print(f"won: {player_row} {player_col}")
elif is_dead:
    print(f"dead: {player_row} {player_col}")

