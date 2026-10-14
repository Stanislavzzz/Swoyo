from fastapi import APIRouter, Query, HTTPException, status, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from schemas.movies import Movie, movie_list_id


router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def movies(
    request: Request,
    year: int = Query(None, description="Год фильма."),
    title: str = Query(None, description="Заголовок фильма.")
):
    """Получить список фильмов."""

    result = movie_list_id
    if title is not None:
        result = [movie for movie in result if title in movie.title]
    if year is not None:
        result = [movie for movie in result if movie.year >= year]

    contex = {
        "title": "Список фильмов !!",
        "movies": result
    }
    return templates.TemplateResponse(request=request, name="movies/movie_list.html", context=contex)


@router.get("/{movie_id}/", response_class=HTMLResponse, name="html_movie_detail")
async def movie_detail(request: Request, movie_id: int):
    """Получить детальную информацию по фильму."""
    movie_id -= 1

    if movie_id < 0 or movie_id >= len(movie_list_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Фильм не найден")

    result = movie_list_id[movie_id]
    contex = {
        "movie": result
    }
    return templates.TemplateResponse(request=request, name="movies/movie_detail.html", context=contex)
#
#
# @router.post("/", response_model=Movie, status_code=status.HTTP_201_CREATED)
# async def movie_create(movie: Movie):
#     """Добавить фильм."""
#
#     for m in movie_list:
#         if m.title == movie.title and m.year == movie.year:
#             raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Такой фильм уже есть")
#
#     movie_list.append(movie)
#
#     return movie
#
#
# @router.put("/{movie_id}/", response_model=Movie)
# async def movie_update(movie_id: int, movie: Movie):
#     """Изменить фильм."""
#     movie_id -= 1
#
#     if movie_id < 0 or movie_id >= len(movie_list):
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Фильм не найден")
#
#     movie_list[movie_id].title = movie.title
#     movie_list[movie_id].year = movie.year
#     return movie_list[movie_id]
#
#
# @router.delete("/{movie_id}/")
# async def movie_delete(movie_id: int):
#     """Удалить фильм."""
#     movie_id -= 1
#
#     if movie_id < 0 or movie_id >= len(movie_list):
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Фильм не найден")
#
#     result = movie_list.pop(movie_id)
#     return {"Message": f"Фильм {result.title} был удален"}


