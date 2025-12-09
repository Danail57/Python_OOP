def inside(r, c, n):
    return 0 <= r < n and 0 <= c < n


moves = {
    "up":    (-1, 0),
    "down":  (1, 0),
    "left":  (0, -1),
    "right": (0, 1)
}

#
n = int(input())
matrix = [list(input()) for _ in range(n)]

spy_r = spy_c = 0
for r in range(n):
    for c in range(n):
        if matrix[r][c] == 'S':
            spy_r, spy_c = r, c
            break

stealth = 100
mission_success = False

while True:
    command = input().strip()

    dr, dc = moves[command]
    nr, nc = spy_r + dr, spy_c + dc

    if not inside(nr, nc, n):
        continue

    matrix[spy_r][spy_c] = '.'

    cell = matrix[nr][nc]


    if cell == 'G':
        stealth -= 40
        if stealth <= 0:
            spy_r, spy_c = nr, nc
            matrix[spy_r][spy_c] = 'S'
            break
        matrix[nr][nc] = '.'
    elif cell == 'B':
        stealth = min(100, stealth + 15)
        matrix[nr][nc] = '.'

    elif cell == 'E':
        mission_success = True
        break

    spy_r, spy_c = nr, nc

    if stealth <= 0:
        matrix[spy_r][spy_c] = 'S'
        break


if stealth <= 0:
    print("Mission failed. Spy compromised.")
else:
    print("Mission accomplished. Spy extracted successfully.")

print(f"Stealth level: {stealth} units")

for row in matrix:
    print("".join(row))
