from copy import deepcopy

name_1 = 'Bob'
name_2 = 'Ivan'
name_3 = 'Mary'
name_4 = 'Alice'

names = [name_1, name_2, name_3, name_4, [1, 2, [10, 10, 11, 15, 17], 3]]
print(names[4][2][-1])


print(names)
print(id(names))

# names_new = names
names_new = names.copy()
names_new = deepcopy(names)
print(names_new)

names_new[0] = 'Kirill'
names_new[-1].append(5)
print(names_new)
print(names)
print(names_new)

print()
print(names)
print(id(names))
print(id(names_new))


