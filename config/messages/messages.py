__all__ = [
    "get_message"
]

MESSAGES: dict[str, dict] = {
    "ru": {
        "gold": "ЗОЛОТО",
        "silver": "СЕРЕБРО",
        "bronze": "БРОНЗА",
        "players_count": "Какое количество игроков?",
        "player_name": "Как зовут игрока #{num}",
        "number_too_small": "Пожалуйста введите число больше чем 1.",
        "name_enter": "Пожалуйста, введите имя.",
        "scores": "Результаты: {players}",
        "not_much_in_cup": "В кубке осталось недостаточно кубиков, "
                           "чтобы {name} смог походить.",
        "turn_player": " {name} ходит.",
        "winner": "Победил {name}!!!",
        "winners": "Победители: {', '.join({names})}",
        "collected": "Звезд собрано: {stars} Черепов собрано: {skulls}",
        "alot_of_skulls": "3 или больше черепа, значит ты потерял свои звезды!",
        "pres_to_continue": "Нажмите Enter для продолжения...",
        "roll_again": "{name}, хотите бросить еще? Y/N",
        "yes_or_no": "Пожалуйста, введите Yes или No.",
        "player_stars": "{name} собрал {stars} звезд!",
        "player_reached_win_score": "{name} набрал {score} очков!!!",
        "extra_turn_notification": "Каждый игрок делает еще один бросок!",
        "end_game": "Игра окончена..."
    },
    "en": {
        "gold": "GOLD",
        "silver": "SILVER",
        "bronze": "BRONZE",
        "players_count": "How many players are there?",
        "player_name": "What is player #{num}'s name?",
        "number_too_small": "Please enter a number larger than 1.",
        "name_enter": "Please enter a name.",
        "scores": "Scores: {players}",
        "not_much_in_cup": "There aren't enough dice left in "
                           "the cup to continue "
                           "{name}'s turn.",
        "turn_player": "It is {name}'s turn.",
        "winner": "The winner is {name}!!!",
        "winners": "The winners are: {', '.join({names})}",
        "collected": "Stars collected: {stars} Skulls collected: {skulls}",
        "alot_of_skulls": "3 or more skulls means you've lost your stars!",
        "pres_to_continue": "Press Enter to continue...",
        "roll_again": "{name}, do you want to roll again? Y/N",
        "yes_or_no": "Please enter Yes or No.",
        "player_stars": "{name} got {stars} stars!",
        "player_reached_win_score": "{name} has reached {score} points!!!",
        "extra_turn_notification": "Everyone else will get one more turn!",
        "end_game": "The game has ended..."
    },
}

def get_message(lang: str, key: str) -> str:
    """
    Функция для получения сообщения по языку и ключу.

    :param lang: ru, en ...
    :param key: Ключ словаря
    :return: Сообщение на выбранном языке
    """
    if lang not in MESSAGES:
        lang = "en"
    return MESSAGES.get(lang, {}).get(
        key,
        "Сообщение не найдено/Message not found")
