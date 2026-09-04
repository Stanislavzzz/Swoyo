class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student {self.name} {self.age=} info!!"


student = Student("Bob", 32)
print(student)