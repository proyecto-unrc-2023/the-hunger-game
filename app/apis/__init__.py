from flask import Blueprint
from flask_restful import Api
from .resources import MenuResource

# Create a blueprint
apis_bp = Blueprint('apis', __name__)
api = Api(apis_bp)

# Registra las rutas
api.add_resource(MenuResource, '/menu')