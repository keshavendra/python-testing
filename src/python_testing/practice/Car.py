class Car:
    wheels = 4
    def __init__(self, color):
        self.color = color

car1 = Car("Red")
car2 = Car("Blue")

print(car1.color)
print(car2.color)
print(car1.wheels)
print(car2.wheels)

Car.wheels = 6

print(car1.wheels)
print(car2.wheels)

car1.wheels = 8

print(car1.wheels)
print(car2.wheels)
print(Car.wheels)