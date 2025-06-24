from llama_index.core import Document


def chunk_players(players: dict) -> list[Document]:
    chunks = []

    for player_id, player in players.items():
        full_name = player.get("full_name", "Unknown Player")
        position = player.get("position", "UNK")
        team = player.get("team", "FA")
        college = player.get("college", "Unknown College")
        age = player.get("age", "?")
        status = player.get("status", "Unknown")

        content = (
            f"{full_name} is a {position} currently listed with team {team}. "
            f"They are {age} years old, played at {college}, and have status '{status}'."
        )

        chunks.append(
            Document(
                text=content,
                metadata={
                    "type": "player_bio",
                    "player_id": player_id,
                    "position": position,
                    "team": team,
                    "college": college,
                    "status": status,
                },
            )
        )

    return chunks


def chunk_rosters(rosters: list) -> list[Document]:
    chunks = []

    for roster in rosters:
        roster_id = roster.get("roster_id")
        owner_id = roster.get("owner_id")
        settings = roster.get("settings", {})
        metadata = roster.get("metadata", {})
        wins = settings.get("wins", 0)
        losses = settings.get("losses", 0)
        ties = settings.get("ties", 0)
        fpts = settings.get("fpts", 0)
        fpts_against = settings.get("fpts_against", 0)

        content = (
            f"Roster {roster_id} (owner {owner_id}) has a record of {wins}-{losses}-{ties}. "
            f"Total points scored: {fpts}, points against: {fpts_against}. "
            f"Streak: {metadata.get('streak')}, Recent performance: {metadata.get('record')}."
        )

        chunks.append(
            Document(
                text=content,
                metadata={
                    "type": "roster_summary",
                    "roster_id": roster_id,
                    "owner_id": owner_id,
                    "league_id": roster.get("league_id"),
                    "wins": wins,
                    "losses": losses,
                },
            )
        )

    return chunks


def chunk_leagues(leagues: list) -> list[Document]:
    chunks = []

    for league in leagues:
        league_name = league.get("name", "Unnamed League")
        season = league.get("season", "unknown")
        scoring = league.get("scoring_settings", {})
        num_teams = league.get("settings", {}).get("num_teams", "?")

        # You can flatten scoring for summarization
        scoring_summary = ", ".join(f"{k}: {v}" for k, v in scoring.items())

        content = (
            f"League '{league_name}' ({season}) has {num_teams} teams. "
            f"Scoring settings: {scoring_summary}."
        )

        chunks.append(
            Document(
                text=content,
                metadata={
                    "type": "league",
                    "season": season,
                    "league_id": league.get("league_id"),
                    "name": league_name,
                },
            )
        )

    return chunks
