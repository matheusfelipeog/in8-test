from flask import Flask

from app import api


def create_app() -> Flask:
    app = Flask(__name__)

    @app.route('/')
    def index():
        return {'status': 'alive'}

    app.register_blueprint(api.bp)

    return app
