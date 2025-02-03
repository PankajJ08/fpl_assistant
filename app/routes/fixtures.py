from flask import Blueprint, jsonify
from app.services.fpl_service import get_upcoming_fixtures

fixtures_bp = Blueprint('fixtures', __name__)

@fixtures_bp.route('/', methods=['GET'])
def upcoming_fixtures():
    return jsonify(get_upcoming_fixtures())
