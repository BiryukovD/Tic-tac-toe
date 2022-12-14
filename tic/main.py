import time
import random

while True:
    playing_field = {'q': [' ', ' 0', ' 1', ' 2'],
                     '0': ['0', '--', '--', '--'],
                     '1': ['1', '--', '--', '--'],
                     '2': ['2', '--', '--', '--']
                                        }
    game_figure = '❌'
    player = 'Игрок №1 ❌'
    robot = False
    end_of_game = False
    game_for_two = False
    game_with_robot = False
    print('Игра "КРЕСТИКИ-НОЛИКИ"\nПример хода: 01, где 0 - номер строки, 1 - номер столбца.')
    count = 0

    y = input('Нажмите "y", чтобы начать игру на двоих или "r", чтобы сыграть с роботом! Ввод: ')
    if y == 'y':
        game_for_two = not game_for_two
    elif y == 'r':
        game_with_robot = not game_with_robot


    print('Поехали! 🔥')

    time.sleep(0.5)

    while game_for_two:
        print(*playing_field['q'])
        print(*playing_field['0'])
        print(*playing_field['1'])
        print(*playing_field['2'])

        try:
            step = input(f'Ваш ход {player}: ')
            if playing_field[step[0]][int(step[1]) + 1] == '❌' or playing_field[step[0]][int(step[1]) + 1] =='🟡':
                continue
            playing_field[step[0]][int(step[1]) + 1] = game_figure
        except:
            continue


        lists = [[playing_field['0'][1], playing_field['0'][2], playing_field['0'][3]],
                 [playing_field['1'][1], playing_field['1'][2], playing_field['1'][3]],
                 [playing_field['2'][1], playing_field['2'][2], playing_field['2'][3]],
                    [playing_field['0'][1], playing_field['1'][1], playing_field['2'][1]],
                    [playing_field['0'][2], playing_field['1'][2], playing_field['2'][2]],
                    [playing_field['0'][3], playing_field['1'][3], playing_field['2'][3]],
                        [playing_field['0'][1], playing_field['1'][2], playing_field['2'][3]],
                        [playing_field['0'][3], playing_field['1'][2], playing_field['2'][1]]]

        for list in lists:
            check_str = ''
            for i in list:
                check_str += i
            if check_str == '❌❌❌' or check_str == '🟡🟡🟡':
                print(*playing_field['q'])
                print(*playing_field['0'])
                print(*playing_field['1'])
                print(*playing_field['2'])
                print(f'Игра окончена победил {player} 🏆')
                time.sleep(2)
                end_of_game = not end_of_game
                break

        if '--' in playing_field['0']:
            pass
        elif '--' in playing_field['1']:
            pass
        elif '--' in playing_field['2']:
            pass
        elif not end_of_game:
            print(*playing_field['q'])
            print(*playing_field['0'])
            print(*playing_field['1'])
            print(*playing_field['2'])
            print("Победила дружба ❤")
            time.sleep(2)
            end_of_game = not end_of_game
            break
        else:
                pass

        if end_of_game:
            break
        game_figure = '🟡' if game_figure == '❌' else '❌'
        player = 'Игрок №2 🟡' if player == 'Игрок №1 ❌' else 'Игрок №1 ❌'

    while game_with_robot:
        print(*playing_field['q'])
        print(*playing_field['0'])
        print(*playing_field['1'])
        print(*playing_field['2'])

        try:
            if robot:
                step = f'{random.randint(0, 2)}{random.randint(0, 2)}'
            else:
                step = input(f'Ваш ход {player}: ')
            if playing_field[step[0]][int(step[1]) + 1] == '❌' or playing_field[step[0]][int(step[1]) + 1] == '🟡':
                continue
            playing_field[step[0]][int(step[1]) + 1] = game_figure
        except:
            continue

        lists = [[playing_field['0'][1], playing_field['0'][2], playing_field['0'][3]],
                 [playing_field['1'][1], playing_field['1'][2], playing_field['1'][3]],
                 [playing_field['2'][1], playing_field['2'][2], playing_field['2'][3]],
                 [playing_field['0'][1], playing_field['1'][1], playing_field['2'][1]],
                 [playing_field['0'][2], playing_field['1'][2], playing_field['2'][2]],
                 [playing_field['0'][3], playing_field['1'][3], playing_field['2'][3]],
                 [playing_field['0'][1], playing_field['1'][2], playing_field['2'][3]],
                 [playing_field['0'][3], playing_field['1'][2], playing_field['2'][1]]]

        for list in lists:
            check_str = ''
            for i in list:
                check_str += i
            if check_str == '❌❌❌' or check_str == '🟡🟡🟡':
                print(*playing_field['q'])
                print(*playing_field['0'])
                print(*playing_field['1'])
                print(*playing_field['2'])
                print(f'Игра окончена победил {player} 🏆')
                time.sleep(2)
                end_of_game = not end_of_game
                break

        if '--' in playing_field['0']:
            pass
        elif '--' in playing_field['1']:
            pass
        elif '--' in playing_field['2']:
            pass
        elif not end_of_game:
            print(*playing_field['q'])
            print(*playing_field['0'])
            print(*playing_field['1'])
            print(*playing_field['2'])
            print("Победила дружба ❤")
            time.sleep(2)
            end_of_game = not end_of_game
            break
        else:
            pass

        if end_of_game:
            break
        game_figure = '🟡' if game_figure == '❌' else '❌'
        player = 'Робот 🟡' if player == 'Игрок №1 ❌' else 'Игрок №1 ❌'
        robot = not robot
        time.sleep(0.5)