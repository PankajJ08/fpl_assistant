import requests
from config import FPL_BASE_URL

# Get all players
def get_all_players():
    url = f"{FPL_BASE_URL}/bootstrap-static/"
    data = requests.get(url).json()
    return data["elements"]

# Get player by name
def get_player_by_name(name):
    players = get_all_players()
    player = next((p for p in players if name.lower() in p["web_name"].lower()), None)
    return player if player else {"error": "Player not found"}

# Get upcoming fixtures
def get_upcoming_fixtures():
    url = f"{FPL_BASE_URL}/fixtures/"
    fixtures = requests.get(url).json()
    return fixtures

# Get all teams
def get_all_teams():
    url = f"{FPL_BASE_URL}/bootstrap-static/"
    data = requests.get(url).json()
    return data["teams"]

# Get gameweek info
def get_gameweek_info(gw_id):
    url = f"{FPL_BASE_URL}/event/{gw_id}/live/"
    try:
        gameweek_data = requests.get(url).json()
        if 'error' in gameweek_data:
            return {"error": f"Failed to fetch data for Gameweek {gw_id}"}
        return gameweek_data
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

# Get user data (team data) by team_id
def get_user_data(team_id):
    url = f"https://fantasy.premierleague.com/api/entry/{team_id}/"
    try:
        user_data = requests.get(url).json()
        return user_data
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

# Get user gameweek score (points for the current gameweek)
def get_user_gameweek_score(team_id):
    url = f"https://fantasy.premierleague.com/api/entry/{team_id}/event/{get_current_gameweek_id()}/picks/"
    try:
        data = requests.get(url).json()
        gameweek_score = sum(player['points'] for player in data['picks'])  # Summing up the points of all players in the team for the gameweek
        return gameweek_score
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

# Get user overall rank
def get_user_overall_rank(team_id):
    url = f"https://fantasy.premierleague.com/api/entry/{team_id}/"
    try:
        user_data = requests.get(url).json()
        return user_data['summary_overall_rank']
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

# Get user league position
def get_user_league_position(team_id, league_id="1161023"):
    url = f"https://fantasy.premierleague.com/api/leagues-classic/{league_id}/standings/"
    try:
        league_data = requests.get(url).json()
        # Find the user position in the league standings
        for i, entry in enumerate(league_data['standings']['results']):
            if entry['entry'] == int(team_id):
                return i + 1  # Position is 1-based
        return {"error": "User not found in the league"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

# Get current gameweek ID
def get_current_gameweek_id():
    url = f"{FPL_BASE_URL}/bootstrap-static/"
    data = requests.get(url).json()
    current_gameweek_id = data['events'][0]['id']  # Assuming the first event is the current gameweek
    return current_gameweek_id

# Get league data by league_id
def get_league_data(league_id):
    url = f"https://fantasy.premierleague.com/api/leagues-classic/{league_id}/standings/"
    try:
        league_data = requests.get(url).json()
        return league_data
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
