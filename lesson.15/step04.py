import requests


city = "Moscow"
api_key = "eddca6f589afb240832059499594ed8b"

url = f"https://api.openweathermap.org/data/2.5/weather/?q={city}&appid={api_key}&units=metric&lang=ru"

# params = {
#     "lang": "ru",
#     "text": "lang",
# }

response = requests.get(url)

# response = requests.get(url, params=params)


if response.ok:
    # print(response.status_code)
    # text = response.text
    # print(text)
    # print(type(text))
    data = response.json().get("main").get("temp")
    print(data)
    print(type(data))



