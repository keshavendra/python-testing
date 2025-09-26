class Flyer:
    def fly(self):
        print("I can fly!")


class Swimmer:
    def swim(self):
        print("I can swim!")


class Duck(Flyer, Swimmer):
    pass


duck = Duck()
duck.fly()
duck.swim()
print(Duck.mro())
