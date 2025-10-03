from functools import reduce

def some_nums(*args):
    return sum(args)

def subtract_nums(*args):
    return reduce(lambda x, y: x - y, args)

def multiply_nums(*args):
    return reduce(lambda x, y: x * y, args)

def divide_nums(*args):
    return reduce(lambda x, y: x / y, args)

mapper= {
    '+': some_nums,
    '-': subtract_nums,
    '*': multiply_nums,
    '/': divide_nums,
}


def operate(sign, *args):
    func = mapper[sign]
    return func(*args)

print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
