import json
from openai import OpenAI

def extract_metadata_filters(prompt: str) -> dict:
    """
    Uses an LLM to extract the 'type' metadata filter from a prompt.

    The 'type' field must be one of: 'league', 'player', or 'roster'.

    Returns:
        A dictionary like: {'type': 'player'} or {} if uncertain.
    """

    system_prompt = """
You are a helpful assistant that identifies the type of information a user is asking about in a fantasy football chat bot.

There are only three possible types:
- "league" → when the user is asking about league-wide rules, standings, formats, info, etc.
- "player" → when the user is asking about a specific player (stats, trades, performance).
- "roster" → when the user is asking about a team’s lineup, roster moves, or composition.

Given a user question, return a JSON object with one field:
{
  "type": "player"
}

Only return one of "league", "player", or "roster". If you’re unsure, return an empty object.
"""

    user_prompt = f'User query: "{prompt}"\n\nReturn metadata as JSON.'

    try:
        response = OpenAI().chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0,
        )

        content = response.choices[0].message.content
        print(f"LLM response: {content}")
        filter_data = json.loads(content.strip())

        if filter_data.get("type") in {"league", "player", "roster"}:
            return filter_data
        else:
            return {}

    except Exception as e:
        print(f"Error parsing LLM response: {e}")
        return {}


def clean_user_query(raw_query: str) -> str:
    """
    Uses an LLM to clean and clarify a raw user query before further processing.
    """

    system_prompt = """
You are a helpful assistant that rewrites raw or informal user queries into clear, structured English.
Preserve the original intent of the query, but correct grammar, clarify vague language, and make it suitable for further processing in a chatbot or search engine.

Do not change the meaning. Do not include any extra explanation. Just return the cleaned-up query as a sentence.
"""

    try:
        response = OpenAI().chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": raw_query},
            ],
            temperature=0.2,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"Error cleaning query: {e}")
        return raw_query
