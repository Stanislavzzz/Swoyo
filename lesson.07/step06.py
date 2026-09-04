from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        """Абстрактный метод, который должен быть реализован."""
        pass

    @abstractmethod
    def walk(self):
        """Абстрактный метод, который должен быть реализован."""
        pass


class Dog(Animal):
    def speak(self):
        return "Гав"

    def walk(self):
        """Абстрактный метод, который должен быть реализован."""
        return "Бежит"


class Cat(Animal):
    def speak(self):
        return "Мяу"

    def walk(self):
        """Абстрактный метод, который должен быть реализован."""
        return "Прыгает"

def make_speak(animal):
    return animal.speak()


dog = Dog()
cat = Cat()
dog1 = Dog()
cat1 = Cat()

# a = Animal()

my_list = [dog, cat, dog1, cat1]
print(my_list)

for item in my_list:
    print(make_speak(item))