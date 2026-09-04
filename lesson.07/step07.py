class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is an person"

    def __repr__(self):
        # return f"{self.name}-{self.age}"
        return f'Person("{self.name}", {self.age})'


p = Person("Bob", 18)
p1 = Person("Alice", 20)

print(p)
print(p1)

my_list = [p, p1]
print(my_list)