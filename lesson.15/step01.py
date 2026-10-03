# GET POST PUT PATCH DELETE
import requests


url = "https://nalog.ru"


response = requests.get(url)
# response = requests.post(url)
# response = requests.put(url)
# response = requests.delete(url)

print(response)
print(response.status_code)
print(response.ok)
print(type(response))

# if response.status_code == 200:
# if response:
if response.ok:
    print(response.status_code)
    print(response.text)

