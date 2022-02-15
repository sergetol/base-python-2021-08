import os

from flask import Flask, render_template
from flask_migrate import Migrate
from werkzeug.exceptions import InternalServerError, NotFound

from models import db
from views.posts import posts_app

app = Flask(__name__)
app.register_blueprint(posts_app, url_prefix="/posts")

app.config.from_object("config.{}".format(os.getenv("CONFIG", "ProdConfig")))

db.init_app(app)

migrate = Migrate(app, db)


@app.route("/", endpoint="index")
def index():
    return render_template("index.html", active_page="index")


@app.route("/about/", endpoint="about")
def about():
    return render_template("about.html", active_page="about")


@app.errorhandler(InternalServerError)
@app.errorhandler(NotFound)
def handle_error(error):
    return render_template("error.html", error=error), error.code


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
