import json


with open('data/employess1.json', 'r', encoding="utf-8") as file:
    try:
        data = json.load(file)
    except json.JSONDecodeError:
        print("Не верный JSON")
        data = {}

print(data)
print(type(data))

print(data.get("country"))
print(data.get("name"))
print(data.get("age"))