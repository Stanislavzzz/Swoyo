my_tuple = (1, 2, 3, [4, 5, 6])
print(my_tuple)
print(type(my_tuple))
print(id(my_tuple))

my_tuple[3].append(7)
print(my_tuple)
print(id(my_tuple))

my_tuple[0] = 5
print(my_tuple)
print(id(my_tuple))

