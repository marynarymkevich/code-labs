import os
import requests
from dotenv import load_dotenv
from api_client import get_json

load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "http://127.0.0.1:8000"

# get all movies
all_movies = get_json(f"{BASE_URL}/movies")
print("Movies list:", all_movies)

# get one movie that does not exist
not_existed_movie = get_json(f"{BASE_URL}/movies/99")

# add a movie
new_movie_data = {
    "title": "Interstellar",
    "director": "Christopher Nolan",
    "year": 2014,
}

headers = {"X-API-Key": API_KEY}
response = requests.post(f"{BASE_URL}/movies", json=new_movie_data, headers=headers, timeout=5)
print(f"POST Status Code: {response.status_code}")
print("Created Movie:", response.json())