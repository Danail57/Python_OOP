class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.speak())

d = Dog()
c = Cat()

animal_sound(d)  
animal_sound(c)  
