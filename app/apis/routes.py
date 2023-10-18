from flask import jsonify
from app.apis import apis_bp

@apis_bp.route("/apis")
def getAllGames():
   return jsonify([])

@apis_bp.route('/apis/<int:game_id>')
def getGame(api_id):
    return jsonify({ 'game': api_id })