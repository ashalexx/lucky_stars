import random

# Установка констант:
GOLD: str = 'GOLD'  # Золото
SILVER: str = 'SILVER'  # Серебро
BRONZE: str = 'BRONZE'  # Бронза

# Графика для звезды, черепа и вопросительного знака:
STAR_FACE: list[str] = ["+-----------+",
                        "|     .     |",
                        "|    ,O,    |",
                        "| 'ooOOOoo' |",
                        "|   `OOO`   |",
                        "|   O' 'O   |",
                        "+-----------+"]
SKULL_FACE: list[str] = ['+-----------+',
                         '|    ___    |',
                         '|   /   \\   |',
                         '|  |() ()|  |',
                         '|   \\ ^ /   |',
                         '|    VVV    |',
                         '+-----------+']
QUESTION_FACE: list[str] = ['+-----------+',
                            '|           |',
                            '|           |',
                            '|     ?     |',
                            '|           |',
                            '|           |',
                            '+-----------+']
FACE_WIDTH: int = 13
FACE_HEIGHT: int = 7

print("""Игра "проверь удачу", в которой вы бросаете кости с изображениями звезд,\
черепов и вопросительных знаков.

На своём ходу вы достаёте три случайные кости из кубка и бросаете их.
Вы можете бросить кости снова или завершить ход. 
Если выпадет три черепа, вы теряете все свои звезды и завершаете ход.

Когда один из игроков наберет 13 очков, игра завершается. 
Побеждает игрок с наибольшим количеством очков.

В кубке 6 золотых, 4 серебряных и 3 бронзовых костей. 
Золотые кости содержат больше звёзд, бронзовые - больше черепов, \
а серебряные сбалансированы.
""")

print('How many players are there?')
while True:  # Цикл до тех пор, пока пользователь не введет число.
    response_players: str = input('> ')
    if response_players.isdecimal() and int(response_players) > 1:
        player_count: int = int(response_players)
        break
    # else:
    print('Please enter a number larger than 1.')

player_names: list[str] = []  # Список имен игроков.
player_scores: dict[str, int] = {}  # Имена игроков как ключи, очки как значения.

for i in range(player_count):
    while True:  # Цикл до тех пор, пока не введено имя.
        print('What is player #' + str(i + 1) + '\'s name?')
        response_players: str = input('> ')
        if response_players != '' and response_players not in player_names:
            player_names.append(response_players)
            player_scores[response_players] = 0
            break
        print('Please enter a name.')

print()

turn: int = 0  # Первый ход у игрока playerNames[0].

# (!) Раскомментируйте, чтобы игрок с именем 'Al' начал с тремя очками:
# player_scores['Al'] = 3

end_game_with: str | None = None  # На счиет этого не уверен

while True:  # Основной игровой цикл.
    print()
    print('SCORES: ', end='')
    for i, name in enumerate(player_names):
        print(name + ' = ' + str(player_scores[name]), end='')
        if i != len(player_names) - 1:
            # Все имена игроков кроме последнего разделяются запятыми.
            print(', ', end='')
    print('\n')

    stars_count: int = 0  # Счетчик собранных звезд.
    skulls_count: int = 0  # Счетчик собранных черепов.
    cup: list[str] = ([GOLD] * 6) + ([SILVER] * 4) + ([BRONZE] * 3)  # Кубок с костями.
    hand: list[str] = []  # Игрок начинает с пустой руки.
    print('It is ' + player_names[turn] + '\'s turn.')

    while True:  # Цикл бросков костей.
        print()
        if (3 - len(hand)) > len(cup):  # Проверка на наличие костей в кубке.
            print('There aren\'t enough dice left in the cup to '
                  + 'continue ' + player_names[turn] + '\'s turn.')
            break

        random.shuffle(cup)  # Перемешивание костей в кубке.
        while len(hand) < 3:
            hand.append(cup.pop())

        roll_results: list[list[str]] = []
        for dice in hand:
            roll: int = random.randint(1, 6)
            if dice == GOLD:
                if 1 <= roll <= 3:
                    roll_results.append(STAR_FACE)
                    stars_count += 1
                elif 4 <= roll <= 5:
                    roll_results.append(QUESTION_FACE)
                else:
                    roll_results.append(SKULL_FACE)
                    skulls_count += 1
            if dice == SILVER:
                if 1 <= roll <= 2:
                    roll_results.append(STAR_FACE)
                    stars_count += 1
                elif 3 <= roll <= 4:
                    roll_results.append(QUESTION_FACE)
                else:
                    roll_results.append(SKULL_FACE)
                    skulls_count += 1
            if dice == BRONZE:
                if roll == 1:
                    roll_results.append(STAR_FACE)
                    stars_count += 1
                elif 2 <= roll <= 4:
                    roll_results.append(QUESTION_FACE)
                else:
                    roll_results.append(SKULL_FACE)
                    skulls_count += 1

        for line_num in range(FACE_HEIGHT):
            for dice_num in range(3):
                print(roll_results[dice_num][line_num] + ' ', end='')
            print()  # Новая строка.

        for dice_type in hand:
            print(dice_type.center(FACE_WIDTH) + ' ', end='')
        print()  # Новая строка.

        print('Stars collected:', stars_count, '  Skulls collected:', skulls_count)

        if skulls_count >= 3:
            print('3 or more skulls means you\'ve lost your stars!')
            input('Press Enter to continue...')
            break

        print(player_names[turn] + ', do you want to roll again? Y/N')
        while True:  # Цикл до ввода Y или N:
            response_players: str = input('> ').upper()
            if response_players != '' and response_players[0] in ('Y', 'N'):
                break
            print('Please enter Yes or No.')

        if response_players.startswith('N'):
            print(player_names[turn], 'got', stars_count, 'stars!')
            player_scores[player_names[turn]] += stars_count

            if end_game_with is None and player_scores[player_names[turn]] >= 13:
                print('\n\n' + ('!' * 60))
                print(player_names[turn] + ' has reached 13 points!!!')
                print('Everyone else will get one more turn!')
                print(('!' * 60) + '\n\n')
                end_game_with: str = player_names[turn]
            input('Press Enter to continue...')
            break

        next_hand: list[str] = []
        for i in range(3):
            if roll_results[i] == QUESTION_FACE:
                next_hand.append(hand[i])  # Сохранение вопросительных знаков.
        hand = next_hand  # Аннотацию делать еще раз, если уже выше анатировано?

    turn = (turn + 1) % player_count  # Переход хода к следующему игроку.

    if end_game_with == player_names[turn]:  # Завершение игры.
        break

print('The game has ended...')

print()
print('SCORES: ', end='')
for i, name in enumerate(player_names):
    print(name + ' = ' + str(player_scores[name]), end='')
    if i != len(player_names) - 1:
        print(', ', end='')
print('\n')

highest_score: int = 0
winners: list[str] = []
for name, score in player_scores.items():
    if score > highest_score:
        highest_score = score
        winners = [name]
    elif score == highest_score:
        winners.append(name)

if len(winners) == 1:
    print('The winner is ' + winners[0] + '!!!')
else:
    print('The winners are: ' + ', '.join(winners))

print('Thanks for playing!')
