from flask import Blueprint, jsonify
from app.services.fpl_service import get_gameweek_info

gameweek_bp = Blueprint('gameweek', __name__)

@gameweek_bp.route('/<int:gw_id>', methods=['GET'])
def gameweek(gw_id):
    # Call the function to get gameweek data and return the result
    gameweek_data = get_gameweek_info(gw_id)
    
    # Return the data as JSON
    return jsonify(gameweek_data)
