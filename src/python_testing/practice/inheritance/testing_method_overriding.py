class Shape:
    def area(self):
        print("Area not defined")

class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rect = Rectangle(10, 5)
print(rect.area())