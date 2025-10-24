def print_top(n):
    for row in range(1, n + 1):
        print(f"{' '*(n-row)}{'* ' * row}")

def print_bottom(n):
    for row in range(1, n):
        print(f"{' '*row}{'* ' * (n-row)}")

print_top(5)
print_bottom(5)
