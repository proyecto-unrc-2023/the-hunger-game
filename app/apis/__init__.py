from flask import Blueprint

# Create a blueprint
apis_bp = Blueprint('apis', __name__)

# Import module routes
from app.apis import routes