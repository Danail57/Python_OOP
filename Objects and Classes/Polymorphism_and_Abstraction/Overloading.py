class MyClass:
    def __init__(self, name, size):
        self.size = size
        self.name = name

    def __len__(self):
        return self.size

my_class = MyClass("Class Name", int(input("Enter size of class: ")))
print(len(my_class))
