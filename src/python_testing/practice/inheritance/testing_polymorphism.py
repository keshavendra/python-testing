class Bird:
    def sound(self):
        return "Chirp"

class Dog:
    def sound(self):
        return "Woof"

class Cat:
    def sound(self):
        return "Meow"

animals = [Bird(), Dog(), Cat()]

for animal in animals:
    print(animal.sound())

