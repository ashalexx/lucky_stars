import random
from typing import Callable

from dice import (
    BRONZE,
    GOLD,
    SILVER,
    check_gold_dice,
    check_bronze_dice,
    check_silver_dice,
    draw_rolls_block,
    show_caption_rolls,
    get_next_hand,
)
from functions import (
    dice_exists,
    fill_player_hand,
    get_players_name,
    print_scores_info,
    get_players_count, print_winners, get_winners
)
from utils import (
    about_game_info
)
from config import (
    PLAYERS_COUNT,
    LANGUAGE,
    GOLD_QUANTITY,
    SILVER_QUANTITY,
    BRONZE_QUANTITY,
    WIN_SCORE,
    get_message
)


def game_logic(player_names: list[str],
               player_scores: dict[str, int],
               num_players: int) -> None:
    end_game_with: str | None = None
    turn: int = 0  # Первый ход у игрока playerNames[0].

    while True:
        print_scores_info(player_names, player_scores)

        stars: int = 0
        skulls: int = 0
        hand: list[str] = []
        # Кубок с костями.
        dice_cup: list[str] = (
                ([GOLD] * GOLD_QUANTITY) +
                ([SILVER] * SILVER_QUANTITY) +
                ([BRONZE] * BRONZE_QUANTITY)
        )

        print(get_message(LANGUAGE, 'turn_player')
              .format(name=player_names[turn]))
        while True:  # Цикл бросков костей.
            print()
            if dice_exists(hand, dice_cup, player_names, turn):
                break

            random.shuffle(dice_cup)
            fill_player_hand(hand, dice_cup)
            callbacks: dict[str, Callable] = {
                GOLD: check_gold_dice,
                SILVER: check_silver_dice,
                BRONZE: check_bronze_dice,
            }

            roll_results = []
            for dice in hand:
                roll = random.randint(1, 6)
                stars, skulls = callbacks.get(dice)(
                    roll_results, roll, stars, skulls
                )

            draw_rolls_block(roll_results)
            show_caption_rolls(hand)

            print(get_message(
                LANGUAGE,
                "collected").format(stars=stars, skulls=skulls))

            if skulls >= 3:
                print(get_message(LANGUAGE, "alot_of_skulls"))
                input(get_message(LANGUAGE, "pres_to_continue"))
                break

            print(
                get_message(
                    LANGUAGE,
                    "roll_again").
                format(name=player_names[turn])
            )
            while True:  # Цикл до ввода Y или N:
                response: str = input("> ").upper()

                if response and response[0] in ("Y", "N"):
                    break

                print(get_message(LANGUAGE, "yes_or_no"))

            if response.startswith("N"):
                print(get_message(
                    LANGUAGE,
                    "player_stars").format(name=player_names[turn], stars=stars))
                player_scores[player_names[turn]] += stars

                if (end_game_with is None and
                        player_scores[player_names[turn]] >= WIN_SCORE):
                    print("\n\n" + ("!" * 60))
                    print(get_message(
                        LANGUAGE,
                        "player_reached_win_score")
                          .format(name=player_names[turn], score=WIN_SCORE))
                    # print(player_names[turn] + f" has reached {WIN_SCORE} points!!!")
                    print(get_message(LANGUAGE, "extra_turn_notification"))
                    # print("Everyone else will get one more turn!")
                    print(("!" * 60) + "\n\n")
                    end_game_with = player_names[turn]
                input(get_message(LANGUAGE, "pres_to_continue"))
                break

            hand = get_next_hand(roll_results, hand)

        # Переход хода к следующему игроку.
        turn = (turn + 1) % num_players

        if end_game_with == player_names[turn]:  # Завершение игры.
            break

    print(get_message(LANGUAGE, "end_game"))


# Имеет смысл на вход функции run() давать lang?
def run() -> None:
    """
    Запуск игры

    :return: None
    """
    about_game_info()
    # lang: str = LANGUAGE
    num_players = PLAYERS_COUNT or get_players_count()
    player_names: list[str] = []
    player_scores: dict[str, int] = {}

    get_players_name(player_names, player_scores, num_players)

    game_logic(player_names, player_scores, num_players)

    winners: list[str] = get_winners(player_scores)
    print_scores_info(player_names, player_scores)
    print_winners(winners)


if __name__ == "__main__":
    run()
