import json


with open('data/employess.json', 'r', encoding="utf-8") as file:
    data = json.load(file)


print(data)
print(type(data))

print(data.get("country"))
print(data.get("name"))
print(data.get("age"))