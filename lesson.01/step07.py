name_1 = 'Bob'
name_2 = 'Ivan'
name_3 = 'Mary'
name_4 = 'Alice'

names = [name_1, name_2, name_3, name_4, 'Serj', 'Petr']

print(names)
print(id(names))

names.pop(0)
print(names)
print(id(names))

names.pop(-1)
print(names)
print(id(names))

name = names.pop()
print(names)
print(id(names))
print(name)
