class PrinterMixin:
    def print_info(self, info):
        print("Info: ", info)

class Student(PrinterMixin):
    def __init__(self, name):
        self.name = name

student = Student("Test")
student.print_info(student.name)

