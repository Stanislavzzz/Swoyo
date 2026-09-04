class Animal:
    def speak(self):
        return "I am an animal"


class Dog(Animal):
    # def speak(self):
    #     return "Гав"
    pass


class Cat(Animal):
    def speak(self):
        return "Мяу"


def make_speak(animal):
    return animal.speak()


dog = Dog()
cat = Cat()
dog1 = Dog()
cat1 = Cat()

a = Animal()

my_list = [dog, cat, dog1, cat1]
print(my_list)

for item in my_list:
    print(make_speak(item))