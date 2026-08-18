person_dict = {
    "name": "Bob",
    "age": 30,
    "prof": ["IT", "Manager", [1, 2, 3, 4, 5]],
}

# print(person_dict.get("city", 'Нет такого города'))

# print(person_dict.keys())
# print(person_dict.values())
# print(person_dict.items())

# for item in person_dict:
# for item in person_dict.keys():
#     print(item)

# for item in person_dict.values():
#     print(item)

# for item in person_dict.items():
# for key, value  in person_dict.items():
#     print(value, key)

# person_dict.clear()
# print(person_dict)
info_dict = {"city": "Moscow", "prof": "street 5 "}

person_dict.update(info_dict)
print(person_dict)