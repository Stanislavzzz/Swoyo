import uvicorn
from fastapi import FastAPI, Query, HTTPException, status
from pydantic import BaseModel


app = FastAPI()


class Movie(BaseModel):
    title: str
    year: int
    description: str


movie_list = [
    Movie(
        title = "Movie1",
        year = 2020,
        description="Description Movie 1"
    ),
    Movie(
        title="Movie2",
        year=1989,
        description="Description Movie 2"
    ),
    Movie(
        title="Movie3",
        year=2015,
        description="Description Movie 3"
    ),
    Movie(
        title="Movie4",
        year=2002,
        description="Description Movie 4"
    ),
    Movie(
        title="Movie5",
        year=2020,
        description="Description Movie 5"
    ),
]


@app.get("/")
async def index():
    return {"message": "Hello World!!!"}


@app.get("/movies/", response_model=list[Movie])
async def movies(
    year: int = Query(None, description="Год фильма."),
    title: str = Query(None, description="Заголовок фильма.")
):
    """Получить список фильмов."""

    result = movie_list
    if title is not None:
        result = [movie for movie in result if title in movie.title]
    if year is not None:
        result = [movie for movie in result if movie.year >= year]

    return result


@app.get("/movies/{movie_id}/", response_model=Movie)
async def movie_detail(movie_id: int):
    """Получить детальную информацию по фильму."""
    movie_id -= 1

    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Фильм не найден")

    result = movie_list[movie_id]
    return result


@app.post("/movies/", response_model=Movie, status_code=status.HTTP_201_CREATED)
async def movie_create(movie: Movie):
    """Добавить фильм."""

    for m in movie_list:
        if m.title == movie.title and m.year == movie.year:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Такой фильм уже есть")

    movie_list.append(movie)

    return movie


@app.put("/movies/{movie_id}/", response_model=Movie)
async def movie_update(movie_id: int, movie: Movie):
    """Изменить фильм."""
    movie_id -= 1

    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Фильм не найден")

    movie_list[movie_id].title = movie.title
    movie_list[movie_id].year = movie.year
    return movie_list[movie_id]


@app.delete("/movies/{movie_id}/")
async def movie_delete(movie_id: int):
    """Удалить фильм."""
    movie_id -= 1

    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Фильм не найден")

    result = movie_list.pop(movie_id)
    return {"Message": f"Фильм {result.title} был удален"}


# @app.get("/movies/{movie_id}/a/{author}/t/{timer}/")
# async def movies(movie_id: int, author: str, timer: int):
#     print(movie_id)
#     print(type(movie_id))
#     print(author)
#     print(type(author))
#     print(timer)
#     print(type(timer))
#     x = movie_id
#     return {"message": f"Movies {x}"}
#
#
# @app.get("/mov/")
# async def movies(
#     name: str = Query(None, description="The name of the movie"),
#     age: int = Query(None, description="The age of the author"),
# ):
#
#     print(name)
#     print(type(name))
#     print(age)
#     print(type(age))
#
#     return {"message": f"Movies {name}"}

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)