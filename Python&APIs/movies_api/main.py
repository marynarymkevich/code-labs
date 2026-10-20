from fastapi import FastAPI, HTTPException

app = FastAPI()

movies = [
    {"id": 1, "title": "Inception", "director": "Christopher Nolan", "year": 2010},
    {"id": 2, "title": "Blade Runner 2049", "director": "Denis Villeneuve", "year": 2017},
    {"id": 3, "title": "Alien", "director": "Ridley Scott", "year": 1979},
    {"id": 4, "title": "The Matrix", "director": "Lana Wachowski", "year": 1999},
]

def find_movie(movie_id: int):
    for movie in movies:
        if movie['id'] == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")

@app.get("/movies")
def get_movies():
    return movies

@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    return find_movie(movie_id)
# Errors 404, 422