from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.director import director_ns
from views.genre import genre_ns
from views.movie import movie_ns


def create_app(config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    app.app_context().push()
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)


app_config = Config()
app = create_app(app_config)
register_extensions(app)


if __name__ == "__main__":
    app.run()