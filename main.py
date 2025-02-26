import logging
import os
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
    get_players_count,
    print_winners,
    get_winners
)
from utils import (
    about_game_info
)
from config import (
    PLAYERS_COUNT,
    GOLD_QUANTITY,
    SILVER_QUANTITY,
    BRONZE_QUANTITY,
    WIN_SCORE,
    get_message
)
from config.gamelog import LOG_DIRS, LOGS_FILE_PATH


def game_logic(player_names: list[str],
               player_scores: dict[str, int],
               num_players: int) -> None:
    end_game_with: str | None = None
    turn: int = 0  # Первый ход у игрока player_names[0].

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

        print(get_message('turn_player')
              .format(name=player_names[turn]))
        while True:  # Цикл бросков костей.
            print()
            if dice_exists(hand, dice_cup, player_names, turn):
                break

            random.shuffle(dice_cup)
            fill_player_hand(hand, dice_cup)
            check_callbacks: dict[str, Callable] = {
                GOLD: check_gold_dice,
                SILVER: check_silver_dice,
                BRONZE: check_bronze_dice,
            }

            roll_results: list[list[str]] = []
            for dice in hand:
                roll = random.randint(1, 6)
                stars, skulls = check_callbacks.get(dice)(
                    roll_results, roll, stars, skulls
                )

            draw_rolls_block(roll_results)
            show_caption_rolls(hand)

            print(
                get_message(
                    "collected"
                ).format(stars=stars, skulls=skulls)
            )

            logger.info(f'Игрок {player_names[turn]}'
                         f' бросил(а) кости: {stars} звезды, {skulls} череп.')

            if skulls >= 3:
                print(get_message("alot_of_skulls"))
                input(get_message("pres_to_continue"))
                break

            print(
                get_message(

                    "roll_again").
                format(name=player_names[turn])
            )
            while True:  # Цикл до ввода Y или N:
                response: str = input("> ").upper()

                if response and response[0] in ("Y", "N"):
                    break

                print(get_message("yes_or_no"))

            if response.startswith("N"):
                print(get_message(

                    "player_stars").format(name=player_names[turn], stars=stars))
                player_scores[player_names[turn]] += stars

                if (end_game_with is None
                        and player_scores[player_names[turn]] >= WIN_SCORE):
                    width_break_line: str = "!" * 60

                    print(f"\n\n{width_break_line}")
                    print(get_message(

                        "player_reached_win_score")
                          .format(name=player_names[turn], score=WIN_SCORE))
                    print(get_message("extra_turn_notification"))
                    print(f"{width_break_line}\n\n")

                    end_game_with = player_names[turn]

                input(get_message("pres_to_continue"))

                break

            hand = get_next_hand(roll_results, hand)

        # Переход хода к следующему игроку.
        turn = (turn + 1) % num_players

        if end_game_with == player_names[turn]:
            break

    print(get_message("end_game"))


def run() -> None:
    """Запуск игры."""
    about_game_info()

    num_players = PLAYERS_COUNT or get_players_count()

    logger.info(f'Игра начата. Кол-во игроков: {num_players}')

    player_names: list[str] = []
    player_scores: dict[str, int] = {}

    get_players_name(player_names, player_scores, num_players)
    game_logic(player_names, player_scores, num_players)

    winners: list[str] = get_winners(player_scores)

    logger.info(f'Игра завершена. Победитель: {winners[0]} с {player_scores[winners[0]]} очками.')

    print_scores_info(player_names, player_scores)
    print_winners(winners)


if __name__ == "__main__":
    os.makedirs(LOG_DIRS, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] [%(levelname)s] %(message)s",
        filename=LOGS_FILE_PATH,
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    logger = logging.getLogger(__name__)

    run()
