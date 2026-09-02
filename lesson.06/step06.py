from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side


def print_shape(shape):
    print(f"Area of shape: {shape.area()}, perimeter: {shape.perimeter()}")


s = Square(10)
c = Circle(10)

print_shape(s)
print_shape(c)


if isinstance(s, Square):
    print("ОК")
if isinstance(c, Square):
    print("ОК")
else:
    print("NO")


if isinstance(123, int):
    print("ОК 123")
else:
    print("NO")