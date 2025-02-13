import json
# from functions import get_players_count

# TODO: Прочитать настройки из json файла,
#  обработать с try/except FileNotFoundError
def read_config(
        data: str
) -> dict[str, int | str, str | str, dict[str, int]] | None:
    """
    Читает конфиг указанного json файла

    :param data: Имя JSON файла
    :return: Преобразованный в словарь JSON файл
    """
    try:
        with open(data, mode="r", encoding="UTF-8") as config:
            return json.load(config)

    except FileNotFoundError:
        print('Такого JSON файла нет!\n'
              'Укажите имя существующего JSON файла.')



config = read_config('config.json')

LANGUAGE: str = config.get("language")
PLAYERS_COUNT: int = config.get("num_players")
GOLD_QUANTITY: int = config.get('dice_in_cup').get('gold')
SILVER_QUANTITY: int = config.get('dice_in_cup').get('silver')
BRONZE_QUANTITY: int = config.get('dice_in_cup').get('bronze')
WIN_SCORE: int = config.get('win_score')


MESSAGES: dict[str, dict] = {
    "ru": {"players_count": "Какое количество игроков?",
           "player_name": "Как зовут игрока #{num}",
           "number_too_small": "Пожалуйста введите число больше чем 1.",
           "name_enter": "Пожалуйста, введите имя.",
           "scores": "Результаты: {players}",
           "not_much_in_cup": "В стаканчике осталось недостаточно кубиков, "
                               "чтобы {name} смог походить.",
           "turn_player": " {name} ходит."
           },
    "en": {"players_count": "How many players are there?",
           "player_name": "What is player #{num}'s name?",
           "number_too_small": "Please enter a number larger than 1.",
           "name_enter": "Please enter a name.",
           "scores": "Scores: {players}",
           "not_much_in_cup": "There aren't enough dice left in "
                               "the cup to continue "
                               "{name}'s turn.",
           "turn_player": "It is {name}'s turn."
           },
}

