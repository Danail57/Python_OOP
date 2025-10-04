class ValueCannotBeNegative(Exception):
    pass

n = int(input())

for _ in range(n):
    number = int(input())
    if number < 0:
        raise ValueCannotBeNegative()
