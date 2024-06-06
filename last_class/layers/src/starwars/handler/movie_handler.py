from flask import Blueprint
from flask import jsonify
from starwars.repository.starwars_client import get_movies

movies_blueprint = Blueprint('movies_blueprint', __name__)


@movies_blueprint.route('/')
def list_movies():
    return jsonify(get_movies())
