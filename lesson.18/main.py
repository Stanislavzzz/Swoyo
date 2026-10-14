import uvicorn
from fastapi import FastAPI

from routers.home import router as home_router
from routers.movies import router as movies_router
from routers.html_movies import router as html_router


app = FastAPI()
app.include_router(home_router, tags=["Main pages"])
app.include_router(movies_router, tags=["Movies"], prefix="/api/v2/movies")
app.include_router(html_router, tags=["HTML Movies"], prefix="/movies")

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)