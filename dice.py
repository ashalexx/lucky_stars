from config import get_message, LANGUAGE

STAR_FACE: list[str] = [
    "+-----------+",
    "|     .     |",
    "|    ,O,    |",
    "| 'ooOOOoo' |",
    "|   `OOO`   |",
    "|   O' 'O   |",
    "+-----------+",
]
SKULL_FACE: list[str] = [
    "+-----------+",
    "|    ___    |",
    "|   /   \\   |",
    "|  |() ()|  |",
    "|   \\ ^ /   |",
    "|    VVV    |",
    "+-----------+",
]
QUESTION_FACE: list[str] = [
    "+-----------+",
    "|           |",
    "|           |",
    "|     ?     |",
    "|           |",
    "|           |",
    "+-----------+",
]

GOLD: str = get_message(LANGUAGE, "gold")
SILVER: str = get_message(LANGUAGE, "silver")
BRONZE: str = get_message(LANGUAGE, "bronze")

FACE_WIDTH: int = 13
FACE_HEIGHT: int = 7


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


def draw_rolls_block(data: list[list[str]]) -> None:
    """
    Выводит изображения выпавших сторон костей.

    :param data: list[list[str]]
    :return: None
    """
    for i in range(FACE_HEIGHT):
        for j in range(3):
            print(data[j][i] + " ", end="")
        print()


def show_caption_rolls(hand: list[str]) -> None:
    """
    Выводит цвета костей.

    :param hand: list[str]
    :return: None
    """
    for dice_type in hand:
        print(dice_type.center(FACE_WIDTH) + " ", end="")
    print()


def get_next_hand(data: list[list[str]], hand: list[str]) -> list[str]:
    """
    Сохранение вопросительных знаков.

    :param data: list[list[str]]
    :param hand: list[str]
    :return: list[str]
    """
    next_hand: list[str] = []
    for i in range(3):
        if data[i] == QUESTION_FACE:
            next_hand.append(hand[i])

    return next_hand
