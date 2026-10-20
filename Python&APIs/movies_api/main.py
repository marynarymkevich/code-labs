from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

movies = [
    {"id": 1, "title": "Inception", "director": "Christopher Nolan", "year": 2010},
    {"id": 2, "title": "Blade Runner 2049", "director": "Denis Villeneuve", "year": 2017},
    {"id": 3, "title": "Alien", "director": "Ridley Scott", "year": 1979},
    {"id": 4, "title": "The Matrix", "director": "Lana Wachowski", "year": 1999},
]

class Movie(BaseModel):
    title: str
    director: str
    year: int

class MovieUpdate(BaseModel):
    title: str | None = None
    director: str | None = None
    year: int | None = None


def find_movie(movie_id: int):
    for movie in movies:
        if movie['id'] == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")


@app.get("/movies")
def get_movies(director: str | None = None, year: int | None = None):
    filtered_movies = []

    for movie in movies:
        if director and director.lower() not in movie["director"].lower():
            continue

        if year and movie["year"] != year:
            continue

        filtered_movies.append(movie)

    return filtered_movies


@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    return find_movie(movie_id)
# Errors 404, 422


@app.post("/movies", status_code=201)
def create_movie(movie: Movie):
    new_id = max((existing_movie["id"] for existing_movie in movies), default=0) + 1
 
    new_movie = {
        "id": new_id,
        "title": movie.title,
        "director": movie.director,
        "year": movie.year
    }
    
    movies.append(new_movie)
    return new_movie


@app.put("/movies/{movie_id}")
def replace_movie(movie_id: int, movie: Movie):
    existing_movie = find_movie(movie_id)
    
    existing_movie["title"] = movie.title
    existing_movie["director"] = movie.director
    existing_movie["year"] = movie.year
    
    return existing_movie


@app.delete("/movies/{movie_id}", status_code=204)
def delete_movie(movie_id: int):
    existing_movie = find_movie(movie_id)
    movies.remove(existing_movie)


@app.patch("/movies/{movie_id}")
def update_movie(movie_id: int, movie_update: MovieUpdate):
    existing_movie = find_movie(movie_id)
    changes = movie_update.model_dump(exclude_unset=True)
    existing_movie.update(changes)
    return existing_movie

## 3 Test the edges
# {} => 200, {"year": "abc"} => 422 Unprocessable Entity, movies/99 => 404 Not Found

# PUT replaces the whole object and requires all fields 
# PATCH updates only the specific fields


