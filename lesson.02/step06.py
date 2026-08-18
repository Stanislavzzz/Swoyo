set_a = {1, 2, 3}
set_b = {3, 5, 7}


set_a.remove(2)
print(set_a)

# set_a.remove(7)
# print(set_a)

set_a.discard(7)
print(set_a)

set_a.add(17)
print(set_a)

print()
print(set_b)
set_b.pop()
print(set_b)

set_b.clear()
print(set_b)
set_b.pop()

# print(id(set_a))
# set_c = set_a.copy()
# print(id(set_c))