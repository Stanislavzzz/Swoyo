
person_dict = {
    "name": "Bob",
    "age": 30,
    "prof": ("IT", "Manager"),
    (1, 2, 3):  True,
    1: "one",
    ("IT1", "Manager1"): 123
}
print(person_dict)
#
# print(person_dict["age"])
# # print(person_dict["age123"])
# print(person_dict.get("age123"))
# print(person_dict.get("age"))


person_dict["age"] += 1
print(person_dict)

person_dict["city"] = "Moscow"
print(person_dict)

del person_dict["prof"]
print(person_dict)

city = person_dict.pop("city")
print(person_dict)
print(city)


city = person_dict.popitem()
print(person_dict)
print(city)
