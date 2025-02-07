import json

# from functions import get_players_count

config = {
    "num_players": 2,
    "win_score": 13,
    "dice_in_cup": {"gold": 6, "silver": 4, "bronze": 3},
    "language": "ru",
}

# TODO: Прочитать настройки из json файла,
#  обработать с try/except FileNotFoundError


# with open("config.json", mode="r", encoding="UTF-8") as config:
#     pass

LANGUAGE: str = config.get("language")
PLAYERS_COUNT: int = config.get(
    "num_players",
    # get_players_count()
)

MESSAGES: dict[str, dict] = {
    "ru": {"players_count": "Сколько количество игроков?"},
    "en": {
        "players_count": "How many players are there?",
        "player_name": "What is player #{num}'s name?",
    },
}
