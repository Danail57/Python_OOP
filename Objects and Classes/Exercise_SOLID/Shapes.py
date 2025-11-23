from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class AreaCalculator:
    def __init__(self, shapes):
        assert isinstance(shapes, list), "`shapes` must be of type list"
        self.shapes = shapes

    @property
    def total_area(self):
        return sum(shape.area() for shape in self.shapes)


shapes = [
    Rectangle(1, 6),
    Triangle(2, 3)
]

calculator = AreaCalculator(shapes)
print("Total area:", calculator.total_area)
