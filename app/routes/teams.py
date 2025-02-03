from flask import Blueprint, jsonify
from app.services.fpl_service import get_all_teams

teams_bp = Blueprint('teams', __name__)

@teams_bp.route('/', methods=['GET'])
def all_teams():
    return jsonify(get_all_teams())
