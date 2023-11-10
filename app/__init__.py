from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import config

jwt = JWTManager()
db = SQLAlchemy(session_options={"expire_on_commit": False})

def create_app(config_name='development'):
    app = Flask(__name__)
    CORS(app)
    
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    db.init_app(app)
     
    #app.secret_key = config[config_name].SECRET_KEY
    jwt.init_app(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    register_modules(app)
    
    return app


def register_modules(app):
    from app.apis import apis_bp

    app.register_blueprint(apis_bp, url_prefix='/game')