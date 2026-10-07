import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from pprint import pprint


url = "https://ru.wikipedia.org/wiki/250_%D0%BB%D1%83%D1%87%D1%88%D0%B8%D1%85_%D1%84%D0%B8%D0%BB%D1%8C%D0%BC%D0%BE%D0%B2_%D0%BF%D0%BE_%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D0%B8_IMDb"
# url = "https://ru.wikipedia.org/wiki/250_250_лучших_фильмов_по_версии_IMDb"

HEADERS = {
    "User-Agent": "MovieParserBot/1.0 (contact: user@mail.com)"
}

response = requests.get(
    url,
    headers=HEADERS,
    timeout=10
)

# print(response.status_code)
# print(response.text)

response.raise_for_status()

# print(response.text)
#
# if "Крёстный отец" in response.text:
#     print("OK")
# else:
#     print("Error")


soup = BeautifulSoup(response.text, "html.parser")
# print(soup)
# print(type(soup))

table = soup.find("table", class_="sortable")
# print(table)
# print(type(table))

rows = table.find_all("tr")
print(len(rows))
# print(rows[0])
# print("*" * 50)
# print(rows[1])


# first_movie_row = rows[1]
# cell = first_movie_row.find_all("td")
# print(len(cell))
#
# rank = cell[0].get_text(" ", strip=True)
# title = cell[1].get_text(" ", strip=True)
# year = cell[2].get_text(" ", strip=True)
# country = cell[3].get_text(" ", strip=True)
# director = cell[4].get_text(" ", strip=True)
#
# print(f"{rank=}")
# print(f"{title=}")
# print(f"{year=}")
# print(f"{country=}")
# print(f"{director=}")

movies = []
for row in rows[1:11]:
    cell = row.find_all("td")
    title_link = cell[1].find("a")

    if title_link is None:
        raise ValueError("Не найдена ссылка на страницу")

    title = title_link.get_text(" ", strip=True)
    href = title_link["href"]

    rank = cell[0].get_text(" ", strip=True)
    year = cell[2].get_text(" ", strip=True)
    country = cell[3].get_text(" ", strip=True)
    director = cell[4].get_text(" ", strip=True)

    movie = {
        "rank": rank,
        "title": title,
        "year": year,
        "country": country,
        "director": director,
        "href": href,
    }
    movies.append(movie)


pprint(movies)

print("*" * 50)
first_movie = movies[0]
print(first_movie)

movie_url = first_movie["href"]
print("*" * 50)

response_movie = requests.get(
    movie_url,
    headers=HEADERS,
    timeout=10
)

print(response_movie.text)
soup_movie = BeautifulSoup(response_movie.text, "html.parser")
info_movie = soup_movie.select_one("section#mwQw")
# info_movie = soup_movie.xpath("//*[@id="Сюжет"]") # для этого надо изменить парсер bs4
print(info_movie)

