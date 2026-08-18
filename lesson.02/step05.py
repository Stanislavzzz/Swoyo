set_a = {1, 2, 3}
set_b = {3, 5, 7}

# union_set = set_a.union(set_b)
union_set = set_a | set_b
print(union_set)
print(type(union_set))

intersection_set = set_a.intersection(set_b)
# intersection_set = set_a & set_b
print(intersection_set)

difference_set = set_a.difference(set_b)
# difference_set = set_a - set_b
print(difference_set)

sym_difference_set = set_a.symmetric_difference(set_b)
# sym_difference_set = set_a ^ set_b
print(sym_difference_set)
