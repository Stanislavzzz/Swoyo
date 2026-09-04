class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        return f"{self.name} выполняет рабочие задачи"

    def __str__(self):
        return f"Сотрудник по имени {self.name}"


class Manager(Employee):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def work(self):
        return f"{self.name} {self.age} управляет командой"


class Developer(Employee):
    def work(self):
        return f"{self.name} пишет код"


e = Employee('Bob')
m = Manager('Alice', 32)
d = Developer('Mary')

print(e)
print(e.work())
print(m)
print(m.work())
print(d)
print(d.work())