class Fibonacci:
    def __init__(self):
        self.cache = {}

    def __call__(self, n):
        if n not in self.cache:
            if n == 0:
                self.cache[0] = 0
            elif n == 1:
                self.cache[1] = 1
            else:
                self.cache[n] = self(n - 1) + self(n - 2)
        return self.cache[n]
fibonacci = Fibonacci()
for i in range(100):
    print(fibonacci(i))
print(fibonacci.cache)
