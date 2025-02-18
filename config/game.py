import json

__all__ = [
    "LANGUAGE",
    "PLAYERS_COUNT",
    "GOLD_QUANTITY",
    "SILVER_QUANTITY",
    "BRONZE_QUANTITY",
    "WIN_SCORE",
]


def read_config(
        filename: str = 'config.json'
) -> dict[str, int | str, str | str, dict[str, int]] | None:
    """
    Читает конфиг указанного json файла.

    :param filename: Имя JSON файла.
    :return: Преобразованный в словарь JSON файл.
    """
    try:
        with open(filename, mode="r", encoding="UTF-8") as config:
            return json.load(config)

    except FileNotFoundError:
        print('Такого JSON файла нет!\n'
              'Укажите имя существующего JSON файла.')


game_config = read_config()

LANGUAGE: str = game_config.get("language")
PLAYERS_COUNT: int = game_config.get("num_players")
GOLD_QUANTITY: int = game_config.get('dice_in_cup').get('gold')
SILVER_QUANTITY: int = game_config.get('dice_in_cup').get('silver')
BRONZE_QUANTITY: int = game_config.get('dice_in_cup').get('bronze')
WIN_SCORE: int = game_config.get('win_score')
