from abc import ABC, abstractmethod



class Quackable(ABC):
    @abstractmethod
    def quack(self):
        pass


class Walkable(ABC):
    @abstractmethod
    def walk(self):
        pass


class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass


class Duck(Quackable, Walkable, Flyable):
    def quack(self):
        return "Quack!"

    def walk(self):
        return "Walking"

    def fly(self):
        return "Flying"




class RubberDuck(Quackable):
    def quack(self):
        return "Squeek"




class RobotDuck(Quackable, Walkable, Flyable):
    HEIGHT = 50

    def __init__(self):
        self.height = 0

    def quack(self):
        return "Robotic quacking"

    def walk(self):
        return "Robotic walking"

    def fly(self):
        """Flies up to a specific height; if reached, lands automatically."""
        if self.height == RobotDuck.HEIGHT:
            self.land()
            return "Reached max height, landing..."

        self.height += 1
        return f"Flying to height {self.height}"

    def land(self):
        self.height = 0


class DuckController:
    """Works with any duck via introduced interfaces (abstract behaviors)."""

    def __init__(self, quackable: Quackable, walkable=None, flyable=None):
        self.quackable = quackable
        self.walkable = walkable
        self.flyable = flyable

    def make_quack(self):
        return self.quackable.quack()

    def make_walk(self):
        if self.walkable:
            return self.walkable.walk()
        return "This duck cannot walk."

    def make_fly(self):
        if self.flyable:
            return self.flyable.fly()
        return "This duck cannot fly."


real_duck = Duck()
rubber_duck = RubberDuck()
robot_duck = RobotDuck()

real_controller = DuckController(real_duck, real_duck, real_duck)
rubber_controller = DuckController(rubber_duck)
robot_controller = DuckController(robot_duck, robot_duck, robot_duck)

print(real_controller.make_quack())
print(real_controller.make_fly())

print(rubber_controller.make_quack())
print(rubber_controller.make_fly())

print(robot_controller.make_walk())
print(robot_controller.make_fly())
