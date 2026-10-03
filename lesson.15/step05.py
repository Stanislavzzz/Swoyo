import requests


city = "Moscow"
api_key = "eddca6f589afb240832059499594ed8b"

url = f"https://api.openweathermap.org/data/2.5/weather/"

params = {
    "q": city,
    "appid": api_key,
    "units": "metric",
    "lang": "ru"
}

response = requests.get(url, params=params)


if response.ok:
    data = response.json().get("main").get("temp")
    print(data)



