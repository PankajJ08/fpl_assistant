from flask import Blueprint, jsonify, request
from app.services.fpl_service import get_league_data

league_bp = Blueprint('league', __name__)

@league_bp.route('/<int:league_id>', methods=['GET'])
def league(league_id):
    league_data = get_league_data(league_id)
    return jsonify(league_data)
