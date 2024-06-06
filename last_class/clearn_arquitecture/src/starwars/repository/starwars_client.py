import requests

movie_url = "https://swapi.dev/api/films/"


def get_movies():
    data = requests.get(movie_url).json()
    movies = [{"id": movie["episode_id"], "name": movie["title"]} for movie in data["results"]]
    return movies
