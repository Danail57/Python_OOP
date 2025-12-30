from abc import ABC, abstractmethod


class Graphic(ABC):
    @abstractmethod
    def draw(self):
        pass


class Circle(Graphic):
    def draw(self):
        print("drawing circle...")

class Rectangle(Graphic):
    def draw(self):
        print("drawing rectangle...")

class CompositeGraphic(Graphic):
    def __init__(self):
        self.__children = []

    def add(self, graphic: Graphic):
        self.__children.append(graphic)

    def remove(self, graphic: Graphic):
        self.__children.remove(graphic)

    def draw(self):
        for child in self.__children:
            child.draw()

c1 = Circle()
c2 = Circle()
r1 = Rectangle()

composite = CompositeGraphic()
composite.add(c1)
composite.add(c2)
composite.add(r1)

composite.draw()
