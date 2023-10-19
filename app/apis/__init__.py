from flask import Blueprint
from flask_restful import Api

# Create a blueprint
apis_bp = Blueprint('apis', __name__)
api = Api(apis_bp)

# Import module routes
from app.apis import routes
from app.apis import apy
