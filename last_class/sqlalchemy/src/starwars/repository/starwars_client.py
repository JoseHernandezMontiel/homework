import requests

movie_url = "https://swapi.dev/api/films/"

def get_movies():
    data = requests.get(movie_url).json()
    movies = [{"id": movie["episode_id"], "name": movie["title"]} for movie in data["results"]]
    return movies


def get_characters_from_movie(episode_id):
    data = requests.get(movie_url).json()
    characters = [{"character": movie["characters"]} for movie in data["results"] if movie["episode_id"] == int(episode_id)]
    return characters