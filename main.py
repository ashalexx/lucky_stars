import random
from typing import Callable

from dice import (
    BRONZE,
    FACE_HEIGHT,
    FACE_WIDTH,
    GOLD,
    QUESTION_FACE,
    SILVER,
    SKULL_FACE,
    STAR_FACE,
    check_gold_dice,
    check_bronze_dice,
    check_silver_dice,
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
from settings import (
    # MESSAGES,
    PLAYERS_COUNT,
    # LANGUAGE,
    GOLD_QUANTITY,
    SILVER_QUANTITY,
    BRONZE_QUANTITY,
    WIN_SCORE
)

# TODO: Поработать над изменениями выводов, чтобы выводился
#  текст на том языка, что из конфигураций


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
    def game_logic():
        end_game_with: str | None = None
        turn: int = 0  # Первый ход у игрока playerNames[0].

        while True:
            print_scores_info(player_names, player_scores)

            stars: int = 0
            skulls: int = 0
            hand: list[str] = []

            dice_cup: list[str] = (
                    ([GOLD] * GOLD_QUANTITY) +
                    ([SILVER] * SILVER_QUANTITY) +
                    ([BRONZE] * BRONZE_QUANTITY)
            )

            cup = dice_cup  # Кубок с костями.

            print("It is " + player_names[turn] + "'s turn.")
            while True:  # Цикл бросков костей.
                print()
                if dice_exists(hand, cup, player_names, turn):
                    break

                random.shuffle(cup)
                fill_player_hand(hand, cup)
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

                # TODO: Продолжим здесь (это для меня)
                for line_num in range(FACE_HEIGHT):
                    for dice_num in range(3):
                        print(roll_results[dice_num][line_num] + " ", end="")
                    print()  # Новая строка.

                for dice_type in hand:
                    print(dice_type.center(FACE_WIDTH) + " ", end="")
                print()  # Новая строка.

                print("Stars collected:", stars, "  Skulls collected:", skulls)

                if skulls >= 3:
                    print("3 or more skulls means you've lost your stars!")
                    input("Press Enter to continue...")
                    break

                print(player_names[turn] + ", do you want to roll again? Y/N")
                while True:  # Цикл до ввода Y или N:
                    response = input("> ").upper()
                    if response != "" and response[0] in ("Y", "N"):
                        break
                    print("Please enter Yes or No.")

                if response.startswith("N"):
                    print(player_names[turn], "got", stars, "stars!")
                    player_scores[player_names[turn]] += stars

                    if (
                            end_game_with == None
                            and player_scores[player_names[turn]] >= 13
                    ):
                        print("\n\n" + ("!" * 60))
                        print(player_names[turn] + " has reached 13 points!!!")
                        print("Everyone else will get one more turn!")
                        print(("!" * 60) + "\n\n")
                        end_game_with = player_names[turn]
                    input("Press Enter to continue...")
                    break

                next_hand = []
                for i in range(3):
                    if roll_results[i] == QUESTION_FACE:
                        next_hand.append(
                            hand[i]
                        )  # Сохранение вопросительных знаков.
                hand = next_hand

            turn = (turn + 1) % num_players  # Переход хода к следующему игроку.

            if end_game_with == player_names[turn]:  # Завершение игры.
                break

        print("The game has ended...")

    game_logic()

    # TODO: вынести за функции run() (в этом модуле остается)
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

    def print_winners() -> None:
        print_scores_info(player_names, player_scores)
        winners: list[str] = get_winners(player_scores)

        if len(winners) == 1:
            print("The winner is " + winners[0] + "!!!")
        else:
            print("The winners are: " + ", ".join(winners))

        print("Thanks for playing!")

    print_winners()


if __name__ == "__main__":
    run()
