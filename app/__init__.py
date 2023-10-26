from flask import Flask
from config import config
from flask_cors import CORS
from flask_restful import Api
from app.apis import apis_bp

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(session_options={"expire_on_commit": False})


def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    CORS(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    config[config_name].init_app(app)

    register_modules(app)
    db.init_app(app)

    return app


def register_modules(app):
    from app.apis import apis_bp
    from app.apis.config_bp import config_bp


    app.register_blueprint(config_bp, url_prefix='/config')