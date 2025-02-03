from flask import Blueprint, jsonify
from app.services.fpl_service import get_all_players, get_player_by_name

players_bp = Blueprint('players', __name__)

@players_bp.route('/', methods=['GET'])
def all_players():
    return jsonify(get_all_players())

@players_bp.route('/<name>', methods=['GET'])
def player_by_name(name):
    return jsonify(get_player_by_name(name))
