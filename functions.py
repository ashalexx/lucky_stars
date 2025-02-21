from config import get_message


def get_players_count() -> int:
    """
    Просит ввести кол-во игроков.

    :return: int
    """
    msg = get_message("players_count")

    print(msg)
    while True:
        count: str = input("> ")
        if count.isdigit() and int(count) > 1:
            return int(count)

        print(get_message('number_too_small'))


def get_players_name(
        names: list[str],
        scores: dict[str, int],
        players_count: int
) -> None:
    """
    Просит ввести имена игроков.

    :param names: Список, где хранятся имена игроков.
    :param scores: Словарь, где ключ = Имя игрока,
    а значение = его очки.
    :param players_count: Количество игроков.
    :return: None
    """
    for i in range(players_count):
        while True:
            print(get_message("player_name").format(num=i + 1))
            name = input("> ")

            if name and name not in names:
                names.append(name)
                scores[name] = 0
                break

            print(get_message("name_enter"))
    print()


def print_scores_info(
        names: list[str],
        scores: dict[str, int]) -> None:
    """
    Выводит результаты игры игроков.

    :param names: List[str]
    :param scores: dict[str, int]
    :return: None
    """
    players: str = ", ".join(f"{name} = {scores[name]}" for name in names)
    print(get_message("scores").format(players=players))


def dice_exists(
        player_hand: list[str],
        dice_cup: list[str],
        names: list[str],
        turn: int
) -> bool:
    """
    Видит сколько кубиков осталось в кубке,
    определяет, можно-ли кидать игроку еще раз.

    :param player_hand: list[str]
    :param dice_cup: list[str]
    :param names: list[str]
    :param turn: int
    :return: bool
    """
    max_dice_count: int = 3

    if (max_dice_count - len(player_hand)) > len(dice_cup):
        print(
            get_message("not_much_in_cup").
            format(name=names[turn])
        )
        return True
    return False


def fill_player_hand(
        player_hand: list[str],
        dice_cup: list[str],
) -> None:
    """
    Пополнение руки игрока кубиками, до 3х штук.

    :param player_hand: list[str]
    :param dice_cup: list[str]
    :return: None
    """
    max_dice_count: int = 3
    while len(player_hand) < max_dice_count:
        player_hand.append(dice_cup.pop())


def get_winners(scores: dict[str, int]) -> list[str]:
    """
    Определяет победителя.

    :param scores: dict[str, int]
    :return: list[str]
    """
    max_score: int = 0
    winners: list[str] = []

    for name, score in scores.items():

        if score > max_score:
            max_score = score
            winners.clear()
            winners.append(name)
        elif score == max_score:
            winners.append(name)

    return winners


def print_winners(winners: list[str]) -> None:
    """
    Выводит имена победителей.

    :param winners: list[str]
    :return: None
    """
    if len(winners) == 1:
        print(get_message("winner").format(name=winners[0]))
    else:
        print(get_message("winners").format(names=winners))

    # TODO: перевод текста.
    print("Thanks for playing!")
