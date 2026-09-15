import json


json_str = """
{
    "country": "Russia",
    "name": "Bob",
    "age": 21,
    "is_empty": true,
    "prof": [
        {
            "IT": "Italian"
        },
        {
            "RU": "Russian"
        }
    ]
}
"""


data = json.loads(json_str)
print(data)
print(type(data))

print(data.get("country"))
print(data.get("name"))
print(data.get("age"))