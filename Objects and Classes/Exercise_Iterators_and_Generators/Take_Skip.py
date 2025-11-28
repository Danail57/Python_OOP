class take_skip:
    def __init__(self, step: int, count: int):
        self.count = count
        self.step = step
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.count:
            value = self.step * self.i
            self.i += 1
            return value
        else:
            raise StopIteration

numbers = take_skip(2, 6)
for number in numbers:
    print(number)
