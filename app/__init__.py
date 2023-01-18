from flask import Flask

from flask_cors import CORS

from app import api


def create_app() -> Flask:
    app = Flask(__name__)
    CORS(app)

    @app.route('/')
    def index():
        return {'status': 'alive'}

    app.register_blueprint(api.bp)

    return app
