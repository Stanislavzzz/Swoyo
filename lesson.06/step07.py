class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):

        return self.__name

    def set_name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self.__name = name
        else:
            print("Не верное имя")


user = Person('Bob', 32)
print(user.get_name())
user.set_name("Mary")

print(user.get_name())
