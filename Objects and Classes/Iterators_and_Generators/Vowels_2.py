class vowels:
    vowels_list = ['a', 'e', 'i', 'o', 'u']

    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.text):
            char = self.text[self.index]
            self.index += 1

            if char.lower() in self.vowels_list:
                return char

        raise StopIteration

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
