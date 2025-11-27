def genrange (start, end):
    while start <= end:
        yield start
        start += 1
# for el in generate(1, 10):
#     print(el)
print(list(genrange (1, 10)))
