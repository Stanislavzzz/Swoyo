import requests


url = "https://httpbin.org/post"

word = "car"
lang = "ru"

params = {
    "word": word,
    "lang": lang
}

data1 = {
    "user_name": "Bob",
    "password": "123qaz",
    "user_age": 32
}

headers = {
    "User-Agent": "SWOYO",
    "Token_SWOYO": "12345qwerty"
}

response = requests.post(url, params=params, data=data1, headers=headers)

if response.ok:
    print(response.request.method)
    print(response.request.url)
    print(response.request.headers)
    print(response.request.body)
    data_resp = response.json()
    print(data_resp)