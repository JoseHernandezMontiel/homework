from flask import Blueprint, request
from flask import jsonify
from starwars.repository.starwars_client import get_movies, get_characters_from_movie
from starwars.repository.movie_repository import SqlAlchemyRepository
from starwars.repository.movie_repository import Movie

movies_blueprint = Blueprint('movies_blueprint', __name__)
repository = SqlAlchemyRepository()


@movies_blueprint.route('/movie/<id>')
def list_movies(id):
    try:
        movie = repository.get(id)
        print(movie.__dict__)
        return jsonify({"id": movie.id, "name": movie.Name})
    except:
        print("Repository error")
        return f"id={id} not found"
    


#http://localhost:3000/movie/2
@movies_blueprint.route('/movie', methods=['POST'])
def list_characters():
    name = request.json['name']
    if name is None:
        return "Invalid request", 400
    
    movie = Movie(Name=name)
    repository.add(movie)
    return name