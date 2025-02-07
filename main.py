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
)
from functions import (
    dice_exists,
    fill_player_hand,
    get_players_name,
    print_game_info,
    print_scores_info,
)
from settings import MESSAGES, PLAYERS_COUNT


def run() -> None:
    """
    Игра "проверь удачу", где вы бросаете кости, чтобы собрать как можно больше звёзд.
    Вы можете бросать кости сколько угодно раз, но если выпадет три черепа, вы теряете все звёзды.

    Игра вдохновлена настольной игрой Zombie Dice - смотреть здесь https://tesera.ru/game/zombie-dice/
    """
    print_game_info()
    lang: str = input(f"Choose language ({', '.join(MESSAGES.keys())}): ")
    numPlayers = PLAYERS_COUNT
    playerNames: list[str] = []
    playerScores: dict[str, int] = {}

    get_players_name(playerNames, playerScores, numPlayers)

    def check_gold_dice(
        data: list[list[str]], roll: int, stars_count: int, skulls_count: int
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

    def check_silver_dice(
        data: list[list[str]], roll: int, stars_count: int, skulls_count: int
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

    def check_bronze_dice(
        data: list[list[str]], roll: int, stars_count: int, skulls_count: int
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

    def game_logic():
        endGameWith: str | None = None
        turn: int = 0  # Первый ход у игрока playerNames[0].

        while True:
            print_scores_info(playerNames, playerScores)

            stars: int = 0
            skulls: int = 0
            hand: list[str] = []
            dice_cup: list[str] = (
                ([GOLD] * 6) + ([SILVER] * 4) + ([BRONZE] * 3)
            )

            cup = dice_cup  # Кубок с костями.

            print("It is " + playerNames[turn] + "'s turn.")
            while True:  # Цикл бросков костей.
                print()
                if dice_exists(hand, cup, playerNames, turn):
                    break

                random.shuffle(cup)
                fill_player_hand(hand, cup)
                callbacks: dict[str, Callable] = {
                    GOLD: check_gold_dice,
                    SILVER: check_silver_dice,
                    BRONZE: check_bronze_dice,
                }

                rollResults = []
                for dice in hand:
                    roll = random.randint(1, 6)
                    stars, skulls = callbacks.get(dice)(
                        rollResults, roll, stars, skulls
                    )

                for lineNum in range(FACE_HEIGHT):
                    for diceNum in range(3):
                        print(rollResults[diceNum][lineNum] + " ", end="")
                    print()  # Новая строка.

                for diceType in hand:
                    print(diceType.center(FACE_WIDTH) + " ", end="")
                print()  # Новая строка.

                print("Stars collected:", stars, "  Skulls collected:", skulls)

                if skulls >= 3:
                    print("3 or more skulls means you've lost your stars!")
                    input("Press Enter to continue...")
                    break

                print(playerNames[turn] + ", do you want to roll again? Y/N")
                while True:  # Цикл до ввода Y или N:
                    response = input("> ").upper()
                    if response != "" and response[0] in ("Y", "N"):
                        break
                    print("Please enter Yes or No.")

                if response.startswith("N"):
                    print(playerNames[turn], "got", stars, "stars!")
                    playerScores[playerNames[turn]] += stars

                    if (
                        endGameWith == None
                        and playerScores[playerNames[turn]] >= 13
                    ):
                        print("\n\n" + ("!" * 60))
                        print(playerNames[turn] + " has reached 13 points!!!")
                        print("Everyone else will get one more turn!")
                        print(("!" * 60) + "\n\n")
                        endGameWith = playerNames[turn]
                    input("Press Enter to continue...")
                    break

                nextHand = []
                for i in range(3):
                    if rollResults[i] == QUESTION_FACE:
                        nextHand.append(
                            hand[i]
                        )  # Сохранение вопросительных знаков.
                hand = nextHand

            turn = (turn + 1) % numPlayers  # Переход хода к следующему игроку.

            if endGameWith == playerNames[turn]:  # Завершение игры.
                break

        print("The game has ended...")

    game_logic()

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

    def print_winners():
        print_scores_info(playerNames, playerScores)
        winners: list[str] = get_winners(playerScores)

        if len(winners) == 1:
            print("The winner is " + winners[0] + "!!!")
        else:
            print("The winners are: " + ", ".join(winners))

        print("Thanks for playing!")


if __name__ == "__main__":
    run()
