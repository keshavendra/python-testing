class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle) :
    def horn(self):
        print("Beep beep!")

obj = Car()
obj.move()
obj.horn()
