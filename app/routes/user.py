from flask import Blueprint, jsonify, request
from app.services.fpl_service import get_user_data

user_bp = Blueprint('user', __name__)

@user_bp.route('/<int:team_id>', methods=['GET'])
def user(team_id):
    user_data = get_user_data(team_id)
    return jsonify(user_data)
