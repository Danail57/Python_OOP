from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


c = Circle(int(input("Enter radius: ")))
s = Square(int(input("Enter side: ")))
s = Square(int(input("Enter a square side: ")))


print("The area of the circle is:", c.area())
print("The area of the square is:", s.area())
