class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary_tuple = tuple(dictionary.items())
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.dictionary_tuple):
            index = self.i
            self.i += 1
            return self.dictionary_tuple[index]
        raise StopIteration

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
