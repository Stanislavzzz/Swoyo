class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __call__(self):
        return f"{self.name} is {self.age} years old"

    def __str__(self):
        return f"{self.name} is an person"


p = Person('Bob', 32)
data = p()
print(data)