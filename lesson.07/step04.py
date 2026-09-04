class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Person {self.name=} {self.age=} info!!"


class Student(Person):
    def __init__(self, name, age, student_number):
        super().__init__(name, age)
        self.student_number = student_number

    def introduce(self):
        return f"{super().introduce()} My student number is {self.student_number=}"


p = Person("Bob", 18)
print(p.introduce())

s = Student("Alice", 20, 123)
print(s.introduce())