class vowels:
    vowels_list = ['a', 'e', 'i', 'o', 'u']

    def __init__(self, text):
        self.text = text
        self.current = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current >= len(self.text):
            raise StopIteration

        char = self.text[self.current]

        if char.lower() in self.vowels_list:
            return char

        return self.__next__() 


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

