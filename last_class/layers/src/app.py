import os
from flask import Flask
from starwars.handler.movie_handler import movies_blueprint



print("Application startup")
port = int(os.getenv('PORT', 3000))
print("PORT::", port)

app = Flask(__name__)
app.register_blueprint(movies_blueprint)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=port)
