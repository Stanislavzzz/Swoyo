empty_tuple = tuple()
print(empty_tuple)
print(type(empty_tuple))

empty_tuple_1 = ()
print(empty_tuple_1)
print(type(empty_tuple_1))


my_tuple = (1, 2, 3)
print(my_tuple)
print(type(my_tuple))
print(id(my_tuple))
my_list = list(my_tuple)
my_list.append(4)
print(my_list)
my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))
print(id(my_tuple))

tuple_one = (1,)
print(tuple_one)
print(type(tuple_one))