import random
from collections.abc import Callable

# from dice import (
#     BRONZE,
#     FACE_HEIGHT,
#     FACE_WIDTH,
#     GOLD,
#     QUESTION_FACE,
#     SILVER,
#     SKULL_FACE,
#     STAR_FACE
# )
from dice import *
# from main import end_game_with


def init_game() -> tuple[list[str], dict[str, int], int]:
    """
    Инициализирует игру, включая ввод количества игроков и их имен.

    :return: player_names, player_scores, player_count
    """
    print('How many players are there?')
    while True:
        response_player = input('> ')
        if response_player.isdecimal() and int(response_player) > 1:
            player_count = int(response_player)
            break
        print('Please enter a number larger than 1.')

    player_names = []
    player_scores = {}

    for i in range(player_count):
        while True:
            print('What is player #' + str(i + 1) + '\'s name?')
            response_player = input('> ')
            if response_player != '' and response_player not in player_names:
                player_names.append(response_player)
                player_scores[response_player] = 0
                break
            print('Please enter a name.')

    return player_names, player_scores, player_count


def has_dice_in_cup(cup: list[str],
                    hand: list[str],
                    player_name: str) -> bool:
    """
    Проверка на наличие костей в кубке

    :param cup: list[str]
    :param hand: list[str]
    :param player_name: str
    :return: bool
    """
    print()
    if (3 - len(hand)) > len(cup):  # Проверка на наличие костей в кубке.
        print('There aren\'t enough dice left in the cup to '
              + 'continue ' + player_name + '\'s turn.')
        return True
    return False


def shuffle_dice_in_cup(cup: list[str],
                        hand: list[str]) -> None:
    """
     Перемешиваем кости в кубке

    :param cup: list[str]
    :param hand: list[int]
    :return: None
    """
    random.shuffle(cup)  # Перемешивание костей в кубке.
    while len(hand) < 3:
        hand.append(cup.pop())


def has_three_skulls(skulls_count: int) -> bool:
    """
    Проверка на 3 черепа в руках игрока

    :param skulls_count: int
    :return: bool
    """
    if skulls_count >= 3:
        print('3 or more skulls means you\'ve lost your stars!')
        input('Press Enter to continue...')
        return True
    return False


def check_gold_dice(
        data: list[list[str]],
        roll: int,
        stars_count: int,
        skulls_count: int
) -> tuple[int, int]:
    """
    Проверяет на выпавшей золотой кости,
    что именно выпало.

    :param data: list[list[str]]
    :param roll: int
    :param stars_count: int
    :param skulls_count: int
    :return: stars_count, skulls_count
    """
    if 1 <= roll <= 3:
        data.append(STAR_FACE)
        stars_count += 1
    elif 4 <= roll <= 5:
        data.append(QUESTION_FACE)
    else:
        data.append(SKULL_FACE)
        skulls_count += 1

    return stars_count, skulls_count


# Проверка серебряной кости
def check_silver_dice(
        data: list[list[str]],
        roll: int,
        stars_count: int,
        skulls_count: int
) -> tuple[int, int]:
    """
    Проверяет на выпавшей серебряной кости,
    что именно выпало.

    :param data: list[list[str]]
    :param roll: int
    :param stars_count: int
    :param skulls_count: int
    :return: stars_count, skulls_count
    """
    if 1 <= roll <= 2:
        data.append(STAR_FACE)
        stars_count += 1
    elif 3 <= roll <= 4:
        data.append(QUESTION_FACE)
    else:
        data.append(SKULL_FACE)
        skulls_count += 1

    return stars_count, skulls_count


# Проверка бронзовой кости
def check_bronze_dice(
        data: list[list[str]],
        roll: int,
        stars_count: int,
        skulls_count: int
) -> tuple[int, int]:
    """
    Проверяет на выпавшей бронзовой кости,
    что именно выпало.

    :param data: list[list[str]]
    :param roll: int
    :param stars_count: int
    :param skulls_count: int
    :return: stars_count, skulls_count
    """
    if roll == 1:
        data.append(STAR_FACE)
        stars_count += 1
    elif 2 <= roll <= 4:
        data.append(QUESTION_FACE)
    else:
        data.append(SKULL_FACE)
        skulls_count += 1

    return stars_count, skulls_count


def roll_dice(
        roll_results: list[list[str]],
        hand: list[str],
        stars_count: int,
        skulls_count: int
) -> tuple[int, int]:
    """
    Отвечает за бросок костей
    и возвращает результаты броска.

    :param roll_results: list[str]
    :param hand: list[str]
    :param stars_count: int
    :param skulls_count: int
    :return: roll_results, stars_count, skulls_count
    """
    callbacks: dict[str, Callable] = {
        GOLD: check_gold_dice,
        SILVER: check_silver_dice,
        BRONZE: check_bronze_dice
    }

    for dice in hand:
        roll = random.randint(1, 6)

        # Использовал колбэки, крутая штука!
        stars_count, skulls_count = callbacks.get(dice)(
            roll_results,
            roll,
            stars_count,
            skulls_count
        )

    return stars_count, skulls_count


def display_scores(player_names: list[str],
                   player_scores: dict[str, int]) -> None:
    """
    Выводит текущие очки всех игроков.

    :param player_names: list[str]
    :param player_scores: dict[str, int]
    :return: None
    """
    print()
    print('SCORES: ', end='')
    for i, name in enumerate(player_names):
        print(name + ' = ' + str(player_scores[name]), end='')
        if i != len(player_names) - 1:
            # Все имена игроков кроме последнего разделяются запятыми.
            print(', ', end='')
    print('\n')


def display_roll_results(roll_results: list[list[str]],
                         hand: list[str],
                         stars_count: int,
                         skulls_count: int) -> None:
    """
    Отображает результаты броска костей.

    :param roll_results: list[list[str]]
    :param hand: ist[str]
    :param stars_count: int
    :param skulls_count: int
    :return: None
    """
    for line_num in range(FACE_HEIGHT):
        for dice_num in range(3):
            print(roll_results[dice_num][line_num] + ' ', end='')
        print()  # Новая строка.

    for dice_type in hand:
        print(dice_type.center(FACE_WIDTH) + ' ', end='')
    print()  # Новая строка.

    print('Stars collected:', stars_count,
          '  Skulls collected:', skulls_count)


def roll_dice_again(player_name: str) -> str:
    """
    Игрок хочет бросить кости еще раз?

    :param player_name: str
    :return: response_player
    """
    print(player_name + ', do you want to roll again? Y/N')
    while True:  # Цикл до ввода Y или N:
        response_player: str = input('> ').upper()
        if response_player != '' and response_player[0] in ('Y', 'N'):
            break
        print('Please enter Yes or No.')
    return response_player


# TODO: решить как изменить переменную end_game_with
def no_in_response(response_player: str,
                   stars_count: int,
                   player_name: str,
                   player_scores: dict[str, int],
                   end_game_with: str | None
                   ) -> str:
    if response_player.startswith('N'):
        print(player_name, 'got', stars_count, 'stars!')
        player_scores[player_name] += stars_count

        if not end_game_with and player_scores[player_name] >= 13:
            print('\n\n' + ('!' * 60))
            print(player_name + ' has reached 13 points!!!')
            print('Everyone else will get one more turn!')
            print(('!' * 60) + '\n\n')
            end_game_with = player_name
        input('Press Enter to continue...')
        return end_game_with
    return ""


# Сохраняем вопросительные знаки
def save_question(hand: list[str],
                  roll_results: list[list[str]]
                ) -> list[str]:
    """
    Сохраняет вопросительные знаки

    :param hand: list[str]
    :param roll_results: list[list[str]]
    :return: оставшиеся вопросительные знаки в руке
    """
    next_hand: list[str] = []
    for i in range(3):
        if roll_results[i] == QUESTION_FACE:
            next_hand.append(hand[i])  # Сохранение вопросительных знаков.
    return next_hand


# Переход хода другому игроку
def switch_player(turn: int, player_count: int) -> int:
    """
    Осуществляет переход кода другому игроку

    :param turn: int
    :param player_count: int
    :return: Следующий игрок
    """
    return (turn + 1) % player_count


# Объявления победителя(ей) и его(их) вывод
def winner(player_scores: dict[str, int]) -> None:
    """
    Выводит имена победителей

    :param player_scores: dict[str, int]
    :return: None
    """
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


