import functions
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

# Инициализация игры
player_names, player_scores, player_count = functions.initialize_game()  # Инициализация игры

turn: int = 0  # Первый ход у игрока player_names[0].
# (!) Раскомментируйте, чтобы игрок с именем 'Al' начал с тремя очками:
# player_scores['Al'] = 3
end_game_with: str | None = None

while True:  # Основной игровой цикл.
    functions.display_scores(player_names, player_scores)

    stars_count: int = 0  # Счетчик собранных звезд.
    skulls_count: int = 0  # Счетчик собранных черепов.
    cup: list[str] = ([GOLD] * 6) + ([SILVER] * 4) + ([BRONZE] * 3)  # Кубок с костями.
    hand: list[str] = []  # Игрок начинает с пустой руки.
    print('It is ' + player_names[turn] + '\'s turn.')

    # functions.player_turn(player_names[turn], cup, player_scores)

    while True:  # Цикл бросков костей.
        print()
        if (3 - len(hand)) > len(cup):  # Проверка на наличие костей в кубке.
            print('There aren\'t enough dice left in the cup to '
                  + 'continue ' + player_names[turn] + '\'s turn.')
            break

        random.shuffle(cup)  # Перемешивание костей в кубке.
        while len(hand) < 3:
            hand.append(cup.pop())

        roll_results, new_stars_count, new_skulls_count = functions.roll_dice(hand)
        stars_count += new_stars_count
        skulls_count += new_skulls_count

        # Отображение результата броска
        functions.display_roll_results(roll_results, hand, stars_count, skulls_count)

        if skulls_count >= 3:
            print('3 or more skulls means you\'ve lost your stars!')
            input('Press Enter to continue...')
            break

        print(player_names[turn] + ', do you want to roll again? Y/N')
        while True:  # Цикл до ввода Y или N:
            response_player: str = input('> ').upper()
            if response_player != '' and response_player[0] in ('Y', 'N'):
                break
            print('Please enter Yes or No.')

        if response_player.startswith('N'):
            print(player_names[turn], 'got', stars_count, 'stars!')
            player_scores[player_names[turn]] += stars_count

            if (end_game_with is None
                    and player_scores[player_names[turn]] >= 13):
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
        hand = next_hand

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

if __name__ == '__main__':
    print('Запуск игры!')
