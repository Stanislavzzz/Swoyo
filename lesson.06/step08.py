class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello {self.name}"


class Child(Parent):
    age = 23

    def greet(self):
        return f"By {self.name}"


parent = Parent("Anna")
print(parent.greet())
# print(parent.age)

child = Child("Bob")
print(child.greet())
print(child.age)
