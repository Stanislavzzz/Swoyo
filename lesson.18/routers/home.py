from fastapi import APIRouter, Query, HTTPException, status


router = APIRouter()


@router.get("/")
async def index():
    return {"message": "Hello World!!!"}


# @router.get("/movies/{movie_id}/a/{author}/t/{timer}/")
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
# @router.get("/mov/")
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
