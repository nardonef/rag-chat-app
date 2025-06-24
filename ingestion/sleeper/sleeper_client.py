import requests
import json
from config import SLEEPER_USER_ID, LEAGUE_YEAR


def fetch_league_data(user_id: str, season: str) -> dict:
    url = f"https://api.sleeper.app/v1/user/{user_id}/leagues/nfl/{season}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def fetch_rosters(league_id: str) -> dict:
    url = f"https://api.sleeper.app/v1/league/{league_id}/rosters"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def fetch_player_info():
    url = "https://api.sleeper.app/v1/players/nfl"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def save_data(data: dict, filename: str):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)


if __name__ == "__main__":
    leagues = fetch_league_data(SLEEPER_USER_ID, LEAGUE_YEAR)
    save_data(leagues, "data/leagues.json")

    if leagues:
        rosters = fetch_rosters(leagues[0]["league_id"])
        save_data(rosters, "data/rosters.json")

    player_info = fetch_player_info()
    save_data(player_info, "data/players.json")
