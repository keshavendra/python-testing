class Employee:

    def __init__(self, name):
        self.name = name
        self.__salary = None

    def set_salary(self, amount):
        if amount > 0 :
            self.__salary = amount

    def get_salary(self):
        return self.__salary