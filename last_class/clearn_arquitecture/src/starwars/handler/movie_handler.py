from flask import Blueprint
from flask import jsonify


def construct_list_movie_handler(actions, repositories):
    movies_blueprint = Blueprint('movies', __name__)

    list_movies = actions["list_movies"]
    client = repositories["starwars_client"]

    @movies_blueprint.route('/')
    def handle():
        return jsonify(list_movies.get(client))

    return movies_blueprint
