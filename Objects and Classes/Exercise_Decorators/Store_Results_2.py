class store_results:
    def __init__(self, filename):
        self.filename = filename

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            with open(self.filename, "a+") as file:
                file.write(f"Function {func.__name__} was called. Result: {func(*args, **kwargs)}\n")
        return wrapper
@store_results("results.txt")
def add(a, b):
    return a + b

@store_results("results.txt")
def mult(a, b):
    return a * b

add(int(input()), int(input()))
mult(int(input()), int(input()))
