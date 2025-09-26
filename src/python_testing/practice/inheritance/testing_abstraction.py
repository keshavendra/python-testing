from abc import abstractmethod, ABC


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.PI * self.radius * self.radius


rec = Rectangle(3, 4)
cir = Circle(7)

print(rec.area())
print(cir.area())
