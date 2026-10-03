import requests



# url = "https://yandex.ru/search/?text=Python"
text = "python"
lang = "ru"
# url = f"https://yandex.ru/search/?text={text}&lang={lang}"
url = f"https://yandex.ru/search/"

params = {
    "lang": "ru",
    "text": "lang",
}

# response = requests.get(url)
response = requests.get(url, params=params)


if response.ok:
    print(response.status_code)
    print(response.text)
    # data = response.json()
    # print(data)



