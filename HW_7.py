"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""

from random import shuffle


def list_generate():
    lst = [i for i in range(1, 91)]
    for _ in range(15):
        lst.append('-')
    shuffle(lst)
    return lst


def card_generate(ind, lst_, round, ):
    if ind == 'player':
        lst_player = lst_
        card = lst_player[(round - 1) * 15:round * 15]
        print('------ Ваша карточка -----')
    elif ind == 'machine':
        lst_machine = lst_
        card = lst_machine[(round - 1) * 15:round * 15]
        print('-- Карточка компьютера ---')
    for j in range(0, 3):
        short_lst = card[j * 5:(j + 1) * 5]
        length = 0
        for n in short_lst:
            length += len(str(n))
        empty_cells = 14 - length
        for _ in range(empty_cells):
            short_lst.append(' ')
        shuffle(short_lst)
        print(*short_lst)
    print('--------------------------')
    return card


def choise_number(lst):
    number = lst.pop()
    return number


def play_cycle():
    lst_player = list_generate()
    lst_machine = list_generate()
    choice_lst = list_generate()
    for number_of_round in range(1, 8):
        print(f"--------- Раунд номер {number_of_round} ------------")
        card_player = card_generate('player', lst_player, number_of_round)
        card_machine = card_generate('machine', lst_machine, number_of_round)
        for i in range(15):
            num = choise_number(choice_lst)
            player_choise = input("Выберите, зачёркиваете ли число на карточке (y) или продолжаете (n):  ")
            print(f'Выбран бочонок номер {num}')
            assert player_choise == 'y' or player_choise == 'n'
            if player_choise == 'y':
                if num in card_player:
                    choise_number(card_player)
                    continue
                else:
                    print("Round over. You lost.")
                    print('***' * 30)
                    break
            if player_choise == 'n':
                if num in card_player:
                    print("Round over. You lost.")
                    print('***' * 30)
                    break
                else:
                    choise_number(card_player)
                    continue
    print("GAME FINISHED")
    print('***' * 30)


play_cycle()
