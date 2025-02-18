__all__ = [
    "MESSAGES",
]

MESSAGES: dict[str, dict] = {
    "ru": {
        "players_count": "Какое количество игроков?",
        "player_name": "Как зовут игрока #{num}",
        "number_too_small": "Пожалуйста введите число больше чем 1.",
        "name_enter": "Пожалуйста, введите имя.",
        "scores": "Результаты: {players}",
        "not_much_in_cup": "В стаканчике осталось недостаточно кубиков, "
                           "чтобы {name} смог походить.",
        "turn_player": " {name} ходит."
    },
    "en": {
        "players_count": "How many players are there?",
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
