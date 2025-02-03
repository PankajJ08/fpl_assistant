from flask import Flask
from app.routes.chatbot import chatbot_bp  # Import the chatbot blueprint
from app.routes.gameweek import gameweek_bp
from app.routes.fixtures import fixtures_bp
from app.routes.players import players_bp
from app.routes.teams import teams_bp
from app.routes.user import user_bp
from app.routes.league import league_bp

def create_app():
    app = Flask(__name__)

    # Register Blueprints for different routes
    app.register_blueprint(chatbot_bp, url_prefix='/chatbot')  # Register chatbot route with prefix /chatbot
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(league_bp, url_prefix='/league')
    app.register_blueprint(gameweek_bp, url_prefix='/gameweek')
    app.register_blueprint(fixtures_bp, url_prefix='/fixtures')
    app.register_blueprint(players_bp, url_prefix='/players')
    app.register_blueprint(teams_bp, url_prefix='/teams')

    return app
