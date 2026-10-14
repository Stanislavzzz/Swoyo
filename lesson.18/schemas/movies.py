from pydantic import BaseModel


class Movie(BaseModel):
    title: str
    year: int
    description: str


class MovieId(Movie):
    pk: int


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

movie_list_id = [
    MovieId(
        pk=1,
        title = "Movie1",
        year = 2020,
        description="Description Movie 1"
    ),
    MovieId(
        pk=2,
        title="Movie2",
        year=1989,
        description="Description Movie 2"
    ),
    MovieId(
        pk=3,
        title="Movie3",
        year=2015,
        description="Description Movie 3"
    ),
    MovieId(
        pk=4,
        title="Movie4",
        year=2002,
        description="Description Movie 4"
    ),
    MovieId(
        pk=5,
        title="Movie5",
        year=2020,
        description="Description Movie 5"
    ),
]