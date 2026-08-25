# def add(x, y):
#     return x + y
#
#
# print(add(1, 8))
# print(add(1, 11))


# def add_el(my_list, value):
#     my_list.append(value)
#     # return my_list
#
#
# nums = [1, 2, 3, 4, 5]
# add_el(nums, 7)
# print(nums)


def update_dict(my_dict, key, value):
    new_dict = my_dict.copy()
    new_dict[key] = value
    return new_dict


info = {"name": "Bob", "age": 30}
print(info)
# new_info = update_dict(info, "city", "Moscow")
new_info = update_dict(key="city", value="Moscow", my_dict=info)

print(info)
print(new_info)
