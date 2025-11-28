def number_increment(numbers):
    def increase():
        return [element + 1 for element in numbers]

    return increase()
print(number_increment([1, 2, 3]))
