from multipledispatch import dispatch

class Person:
    def __init__(self, name, age, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, student_id, **kwargs):
        super().__init__(**kwargs)
        self.student_id = student_id

    def display_info(self):
        print(f"Student Name: {self.name}, Age: {self.age}, ID: {self.student_id}")

class Lecturer(Person):
    def __init__(self, employee_id, **kwargs):
        super().__init__(**kwargs)
        self.employee_id = employee_id
        self.salary = 12000

    def display_info(self):
        print(f"Lecturer Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}")

# Method overloading using multipledispatch
@staticmethod
@dispatch(str, int)
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

class Staff(Student, Lecturer):
    def __init__(self, staff_id, **kwargs):
        super().__init__(**kwargs)
        self.staff_id = staff_id

    def display_info(self):
        print(f"Staff Name: {self.name}, Age: {self.age}, "
              f"Student ID: {self.student_id}, Employee ID: {self.employee_id}, "
              f"Staff ID: {self.staff_id}")

# Now run everything
print("\nDemonstration of method overriding")
student = Student(name="Amber", age=20, student_id="O12")
student.display_info()

print("\nDemonstration of method overloading")
lecturer = Lecturer(name="Dr. Smith", age=40, employee_id="E123")
lecturer.display_info()

print("\nDemonstration of method overloading with multipledispatch")
display_info("Alice", 30)

print("\nDemonstration of mro")
staff = Staff(name="Rain", age=8, student_id="S01", employee_id="E01", staff_id="ST01")
staff.display_info()

print("\nMethod Resolution Order (MRO):")
for cls in Staff.__mro__:
    print(cls)
