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

GOLD: str = "GOLD"
SILVER: str = "SILVER"
BRONZE: str = "BRONZE"

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
