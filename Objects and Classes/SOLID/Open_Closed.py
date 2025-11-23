
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    
class Dog(Animal):
    def make_sound(self):
        return "Woof!"
    
class Cat(Animal):
    def make_sound(self):
        return "Meow!"
    
class Parrot(Dog):
    def make_sound(self):
        return "I'm a parrot!"

class Pig(Animal):
    def make_sound(self):
        return "Gruh!"

# function is closed for changes
def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Dog(), Cat(), Parrot()]
animal_sound(animals)
