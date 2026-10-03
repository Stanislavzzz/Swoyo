import requests

import config


def get_weather_data(city):
    api_key = config.TOKEN_WEATHER
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
        return data


if __name__ == '__main__':
    city = "Тула"
    temp = get_weather_data(city)
    print(temp)
