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

        print(MESSAGES.get(LANGUAGE).get('number_too_small'))


def get_players_name(
    names: list[str],
    scores: dict[str, int],
    players_count: int
) -> None:
    for i in range(players_count):
        while True:
            print(MESSAGES.get(LANGUAGE).get("player_name").format(num=i + 1))
            name = input("> ")

            if name and name not in names:
                names.append(name)
                scores[name] = 0
                break

            print(MESSAGES.get(LANGUAGE).get("name_enter"))
    print()


def print_scores_info(names, scores):
    players: str = ", ".join(f"{name} = {scores[name]}" for name in names)
    print(MESSAGES.get(LANGUAGE).get("scores").format(players = players))


def dice_exists(
    player_hand: list[str],
    dice_cup: list[str],
    names: list[str],
    turn: int
) -> bool:
    max_dice_count: int = 3

    if (max_dice_count - len(player_hand)) > len(dice_cup):
        print(
            MESSAGES.get(LANGUAGE).get("not_much_in_cup").
            format(name=names[turn])
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
