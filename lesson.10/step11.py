import json


employess = {
  "country": "Russia",
  "name": "Bob",
  "age": 21,
  "is_empty": True,
  "prof": [
      {"IT": "Italian"},
      {"RU": "Russian"}
  ]
}
print(employess)
print(type(employess))

# json_str = json.dumps(employess)
# print(json_str)

json_str = json.dumps(employess, indent=4)
print(json_str)
