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

with open('./data/employess.json', 'w', encoding="utf-8") as file:
    json.dump(employess, file, ensure_ascii=False, indent=4)
