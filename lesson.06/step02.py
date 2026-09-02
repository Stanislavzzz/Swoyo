class Fruit:
    pass


a = Fruit()
b = Fruit()

# print(a)
# print(id(a))
# print(type(a))
# print(b)
# print(id(b))
# print(type(b))

a.name = "apple"
a.weight = 120


b.name = "banana"
b.weight = 170

print(a.name)
print(b.name)
# print(b.age)\
a.weight -= 100
print(a.weight)
