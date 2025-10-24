def print_top(n):
    for row in range(1, n + 1):
        print(' ' * (n - row) + '* ' * row)

def print_bottom(n):
    for row in range(n - 1, 0, -1):
        print(' ' * (n - row) + '* ' * row)

n = int(input())
print_top(n)
print_bottom(n)
