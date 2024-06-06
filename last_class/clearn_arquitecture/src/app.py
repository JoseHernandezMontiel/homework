import os
from flask import Flask
from starwars.repository import repository_list
from starwars.actions import action_list
from starwars.handler.movie_handler import construct_list_movie_handler

print("Application startup")
port = int(os.getenv('PORT', 3000))
print("PORT::", port)

app = Flask(__name__)
app.register_blueprint(construct_list_movie_handler(action_list, repository_list))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=port)
