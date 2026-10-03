import requests


url = "https://randomfox.ca/floof/"


response = requests.get(url)


if response.ok:
    print(response.status_code)
    # print(response.text)
    data = response.json()
    print(data)



