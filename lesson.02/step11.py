
my_list = [1, 2, 3, 3, 2, 1, 1, 2]
my_tuple = (1, 2, 3, [4, 5, 6])
set_a = {1, 2, 3}
person_dict = {
    "name": "Bob",
    "age": 30,
    "prof": ["IT", "Manager", [1, 2, 3, 4, 5]],

}

# for item in my_list:
#     print(item)

# for item in my_tuple:
#     print(item)

# for item in set_a:
#     print(item)

# for item in person_dict:
#     print(item)

if 1 in my_list:
    print("1 is in my_list")

if 1 in my_tuple:
    print("1 is in my_tuple")

if 1 in set_a:
    print("1 is in set_a")

if "name1" in person_dict:
    print("name is in person_dict")