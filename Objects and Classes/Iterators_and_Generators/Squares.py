def squares(end):
    num = 1
    while num <= end:
        yield num * num
        num += 1
# for element in squares(5):
#     print(element)

print(list(squares(5)))
