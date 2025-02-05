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
# player_scores['Al'] = 3
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

        # TODO: Функция вопроса, хочет-ли игрок еще бросить кости
        print(player_names[turn] + ', do you want to roll again? Y/N')
        while True:  # Цикл до ввода Y или N:
            response_player: str = input('> ').upper()
            if response_player != '' and response_player[0] in ('Y', 'N'):
                break
            print('Please enter Yes or No.')

        # TODO: Функция если он ответил 'N'
        if response_player.startswith('N'):
            print(player_names[turn], 'got', stars_count, 'stars!')
            player_scores[player_names[turn]] += stars_count

            if (end_game_with is None
                    and player_scores[player_names[turn]] >= 13):
                print('\n\n' + ('!' * 60))
                print(player_names[turn] + ' has reached 13 points!!!')
                print('Everyone else will get one more turn!')
                print(('!' * 60) + '\n\n')
                end_game_with: str = player_names[turn]
            input('Press Enter to continue...')
            break

        next_hand: list[str] = []
        for i in range(3):
            if roll_results[i] == QUESTION_FACE:
                next_hand.append(hand[i])  # Сохранение вопросительных знаков.
        hand = next_hand

    turn = (turn + 1) % player_count  # Переход хода к следующему игроку.

    if end_game_with == player_names[turn]:  # Завершение игры.
        break

print('The game has ended...')

functions.display_scores(player_names, player_scores)

highest_score: int = 0
winners: list[str] = []
for name, score in player_scores.items():
    if score > highest_score:
        highest_score = score
        winners = [name]
    elif score == highest_score:
        winners.append(name)

if len(winners) == 1:
    print('The winner is ' + winners[0] + '!!!')
else:
    print('The winners are: ' + ', '.join(winners))

print('Thanks for playing!')
