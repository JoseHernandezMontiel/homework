from flask import Flask

from controllers.ItemController import item_controller_blueprint
from views.Item import item_views_blueprint

app = Flask(__name__)

app.register_blueprint(item_controller_blueprint)
app.register_blueprint(item_views_blueprint)

if __name__ == '__main__':
   app.run(host="0.0.0.0", debug=True, port=80)