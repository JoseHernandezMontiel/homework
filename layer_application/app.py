from flask import Blueprint, Flask
from controllers.itemController import destroy, index, show, store

app = Flask(__name__)

blueprint = Blueprint('blueprint', __name__)


# POST
blueprint.route('/item', methods=['POST'])(store)

# GET
blueprint.route('/items', methods=['GET'])(index)

blueprint.route('/item/<id>', methods=['GET'])(show)

# DELETE
blueprint.route('/item/<id>', methods=['DELETE'])(destroy)


app.register_blueprint(blueprint)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True, port=8081)