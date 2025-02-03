from flask import Blueprint, jsonify, request, render_template
from app.services.fpl_service import get_gameweek_info, get_player_by_name, get_upcoming_fixtures, get_user_gameweek_score, get_user_overall_rank, get_user_league_position

chatbot_bp = Blueprint('chatbot', __name__)

@chatbot_bp.route('/', methods=['GET'])
def chatbot_ui():
    return render_template('chatbot.html')


def get_user_fpl_id():
    return "4333543"

    
@chatbot_bp.route('/ask', methods=['POST'])
def ask_question():
    user_question = request.json.get('question', '').lower()

    if not user_question:
        return jsonify({"answer": "Please ask a valid question."})

    # Detect intent
    if 'gameweek' in user_question or 'gw' in user_question:
        gw_id = extract_gameweek_number(user_question)
        if gw_id:
            gameweek_data = get_gameweek_info(gw_id)
            return jsonify({"answer": format_gameweek_data(gameweek_data)})
        else:
            return jsonify({"answer": "Please specify a valid gameweek number."})

    elif 'player' in user_question:
        player_name = extract_player_name(user_question)
        if player_name:
            player_data = get_player_by_name(player_name)
            
            print("DEBUG: Player API Response:", player_data)  # Check API response in terminal
            
            if player_data:
                return jsonify({"answer": format_player_data(player_data)})
            else:
                return jsonify({"answer": f"Could not find data for player '{player_name}'."})
        else:
            return jsonify({"answer": "Please specify a valid player name."})

    elif 'fixtures' in user_question:
        fixtures = get_upcoming_fixtures()
        return jsonify({"answer": format_fixtures_data(fixtures)})

    elif 'points this week' in user_question or 'gameweek score' in user_question:
        user_id = get_user_fpl_id()  # Assuming you have a way to get the user’s FPL ID
        gameweek_score = get_user_gameweek_score(user_id)
        return jsonify({"answer": f"Your score for this Gameweek is: {gameweek_score} points 🏆"})

    elif 'overall rank' in user_question:
        user_id = get_user_fpl_id()
        overall_rank = get_user_overall_rank(user_id)
        return jsonify({"answer": f"Your overall rank is: {overall_rank} 🌍"})

    elif 'league position' in user_question:
        user_id = get_user_fpl_id()
        league_position = get_user_league_position(user_id)
        return jsonify({"answer": f"Your position in the league is: {league_position} 🏅"})

    else:
        return jsonify({"answer": "Sorry, I didn't understand your question. Try asking about players, gameweeks, or fixtures."})

# Helper function to extract gameweek number from text
def extract_gameweek_number(question):
    words = question.split()
    for i, word in enumerate(words):
        if word in ['gameweek', 'gw'] and i + 1 < len(words):
            if words[i + 1].isdigit():
                return int(words[i + 1])
    return None

# Helper function to extract player name
def extract_player_name(question):
    words = question.split()
    if 'player' in words:
        index = words.index('player') + 1
        return ' '.join(words[index:]) if index < len(words) else None
    return None

# Format player data for better display
def format_player_data(player_data):
    if not player_data:
        return "No player data found."
    
    return (
        f"**{player_data.get('name', 'Unknown')}**\n"
        f"🏆 Team: {player_data.get('team', 'Unknown')}\n"
        f"⚽ Total Points: {player_data.get('total_points', 'N/A')}\n"
        f"📊 Selected by: {player_data.get('selected_by_percent', 'N/A')}%"
    )

# Format gameweek data for better display
def format_gameweek_data(gameweek_data):
    if not gameweek_data:
        return "No gameweek data found."
    
    return (
        f"📅 **Gameweek {gameweek_data.get('id', 'Unknown')}**\n"
        f"📆 Deadline: {gameweek_data.get('deadline_time', 'Unknown')}\n"
        f"🎯 Average Points: {gameweek_data.get('average_entry_score', 'N/A')}"
    )

# Format fixtures data for better display
def format_fixtures_data(fixtures):
    if not fixtures:
        return "No upcoming fixtures available."
    
    formatted_fixtures = "\n".join([
        f"🏟 {fixture['home_team']} vs {fixture['away_team']} - {fixture['kickoff_time']}"
        for fixture in fixtures
    ])
    return f"📅 **Upcoming Fixtures:**\n{formatted_fixtures}"
