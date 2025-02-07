from settings import LANGUAGE, MESSAGES

# TODO: Поработать над изменениями выводов, чтобы выводился
#  текст на том языка, что из конфигураций

def get_players_count() -> int:
    msg = MESSAGES.get(LANGUAGE).get("players_count")

    print(msg)
    while True:
        count: str = input("> ")
        if count.isdigit() and int(count) > 1:
            return int(count)

        print("Please enter a number larger than 1.")


def get_players_name(
    names: list[str], scores: dict[str, int], players_count: int
) -> None:
    for i in range(players_count):
        while True:
            print(MESSAGES.get("en").get("player_name").format(num=i + 1))
            name = input("> ")

            if name and name not in names:
                names.append(name)
                scores[name] = 0
                break

            print("Please enter a name.")
    print()


# TODO: Приводить к PEP8
def print_game_info() -> None:
    print(
        """Игра "проверь удачу", в которой вы бросаете кости с изображениями звезд, черепов и вопросительных знаков.

        На своём ходу вы достаёте три случайные кости из кубка и бросаете их. Вы можете бросить кости снова или завершить ход.
        Если выпадет три черепа, вы теряете все свои звезды и завершаете ход.

        Когда один из игроков наберет 13 очков, игра завершается. Побеждает игрок с наибольшим количеством очков.

        В кубке 6 золотых, 4 серебряных и 3 бронзовых костей. Золотые кости содержат больше звёзд, бронзовые - больше черепов, а серебряные сбалансированы.
        """
    )


def print_scores_info(names, scores):
    players: str = ", ".join(f"{name} = {scores[name]}" for name in names)
    print(f"\nScores: {players}")


def dice_exists(
    player_hand: list[str], dice_cup: list[str], names: list[str], turn: int
) -> bool:
    max_dice_count: int = 3

    if (max_dice_count - len(player_hand)) > len(dice_cup):
        print(
            "There aren't enough dice left "
            "in the cup to continue " + names[turn] + "'s turn."
        )
        return True
    return False


def fill_player_hand(
    player_hand: list[str],
    dice_cup: list[str],
) -> None:
    max_dice_count: int = 3
    while len(player_hand) < max_dice_count:
        player_hand.append(dice_cup.pop())
