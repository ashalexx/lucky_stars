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
    get_players_count
)
from utils import (
    about_game_info
)
from config import (
    PLAYERS_COUNT,
    LANGUAGE,
    MESSAGES,
    GOLD_QUANTITY,
    SILVER_QUANTITY,
    BRONZE_QUANTITY,
    WIN_SCORE
)


def get_winners(scores: dict[str, int]) -> list[str]:
    max_score: int = 0
    winners: list[str] = []

    for name, score in scores.items():
        if score > max_score:
            max_score = score
            winners = [name]
        elif score == max_score:
            winners.append(name)

    return winners


def print_winners(
        name: list[str],
        scores: dict[str, int]) -> None:
    print_scores_info(name, scores)
    winners: list[str] = get_winners(scores)

    if len(winners) == 1:
        print("The winner is " + winners[0] + "!!!")
    else:
        print("The winners are: " + ", ".join(winners))

    print("Thanks for playing!")


# TODO: Поработать над изменениями выводов, чтобы выводился
#  текст на том языка, что из конфигураций


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

        print(MESSAGES.get(LANGUAGE).get('turn_player')
              .format(name=player_names[turn]))
        print("It is " + player_names[turn] + "'s turn.")
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

            print("Stars collected:", stars, "  Skulls collected:", skulls)

            if skulls >= 3:
                print("3 or more skulls means you've lost your stars!")
                input("Press Enter to continue...")
                break

            print(player_names[turn] + ", do you want to roll again? Y/N")
            while True:  # Цикл до ввода Y или N:
                response: str = input("> ").upper()

                if response and response[0] in ("Y", "N"):
                    break

                print("Please enter Yes or No.")

            if response.startswith("N"):
                print(player_names[turn], "got", stars, "stars!")
                player_scores[player_names[turn]] += stars

                if end_game_with is None and player_scores[player_names[turn]] >= WIN_SCORE:
                    print("\n\n" + ("!" * 60))
                    print(player_names[turn] + f" has reached {WIN_SCORE} points!!!")
                    print("Everyone else will get one more turn!")
                    print(("!" * 60) + "\n\n")
                    end_game_with = player_names[turn]
                input("Press Enter to continue...")
                break

            hand = get_next_hand(roll_results, hand)

        # Переход хода к следующему игроку.
        turn = (turn + 1) % num_players

        if end_game_with == player_names[turn]:  # Завершение игры.
            break

    print("The game has ended...")


# TODO: Убрать или переписать документацию к функции run()
def run() -> None:
    """
    Запуск игры

    :return: None
    """
    about_game_info()
    # lang: str = LANGUAGE  # Параллельный импорт, как избежать?
    # Корректно ли так делать?
    num_players = PLAYERS_COUNT or get_players_count()
    player_names: list[str] = []
    player_scores: dict[str, int] = {}

    get_players_name(player_names, player_scores, num_players)
    # TODO: вынести за функции run() (в этом модуле остается)
    game_logic(player_names, player_scores, num_players)
    print_winners(player_names, player_scores)


if __name__ == "__main__":
    run()
