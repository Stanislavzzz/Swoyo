name_1 = 'Bob'
name_2 = 'Ivan'
name_3 = 'Mary'
name_4 = 'Alice'

names = [name_1, name_2, name_3, name_4, 'Serj', 'Ivan', 'Petr', 'Ivan']

print(names)
print(id(names))

names.remove('Ivan')
print(names)
print(id(names))

my_name = 'Mary123'
if my_name in names:
    name = names.remove(my_name)

print(names)
print(id(names))


print(names.count('Ivan123'))
print(names.index('Alice'))