import functions
from dice import (
    BRONZE,
    FACE_HEIGHT,
    FACE_WIDTH,
    GOLD,
    QUESTION_FACE,
    SILVER,
    SKULL_FACE,
    STAR_FACE
)
from dice import *

from utils import about_game_info

about_game_info()

# Инициализация игры
player_names, player_scores, player_count = functions.init_game()

turn: int = 0  # Первый ход у игрока player_names[0].
# (!) Раскомментируйте, чтобы игрок с именем 'Al' начал с тремя очками:
# player_scores['Al'] = 13
end_game_with: str | None = None

# TODO: Функцию основного цикла игры
while True:  # Основной игровой цикл.
    functions.display_scores(player_names, player_scores)

    stars_count: int = 0  # Счетчик собранных звезд.
    skulls_count: int = 0  # Счетчик собранных черепов.

    cup: list[str] = (([GOLD] * GOLD_DICE_QUANTITY) +
                      ([SILVER] * SILVER_DICE_QUANTITY) +
                      ([BRONZE] * BRONZE_DICE_QUANTITY))  # Кубок с костями.
    hand: list[str] = []  # Игрок начинает с пустой руки.

    print('It is ' + player_names[turn] + '\'s turn.')

    while True:  # Цикл бросков костей.

        # Проверка на наличие костей в кубке
        functions.has_dice_in_cup(cup, hand, player_names[turn])

        # Перемешивания костей в кубке
        functions.shuffle_dice_in_cup(cup, hand)

        roll_results: list[list[str]] = []

        # Бросок костей
        stars_count, skulls_count = functions.roll_dice(
            roll_results,
            hand,
            stars_count,
            skulls_count
        )

        # Отображение результата броска
        functions.display_roll_results(roll_results,
                                       hand,
                                       stars_count,
                                       skulls_count)

        # Проверка на 3 черепа
        if functions.has_three_skulls(skulls_count):
            break

        # Хочет-ли игрок бросить кости еще раз?
        response_player = functions.roll_dice_again(player_names[turn])

        # Если пользователь ответил НЕТ
        if functions.no_in_response(response_player,
                                    stars_count,
                                    player_names[turn],
                                    player_scores,
                                    end_game_with
                                    ):
            break

        # Сохраняет вопросительные знаки
        hand = functions.save_question(hand, roll_results)

    # Переход хода к другому игроку
    turn = functions.switch_player(turn, player_count)

    # TODO: Функция конца игры
    if end_game_with == player_names[turn]:  # Завершение игры.
        break

print('The game has ended...')

functions.display_scores(player_names, player_scores)

# Объявления победителя(ей) и его(их) вывод
functions.winner(player_scores)
