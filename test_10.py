#Rock_Paper_Scissors
import random

def my_input():

    while True:
        try:
            var = input("\nВыберите Камень (R), Бумага (P), Ножницы(S): ").lower()
        except ValueError:
            print("\nАлгоритм принимает только строки!")
        else:
            if var == 'r':
                break
            elif var == 'p':
                break
            elif var == 's':
                break
            elif var == 'q':
                break

    return var

def find_winner(user_input, sys_input):

    if user_input == sys_input:
        return None

    elif (user_input == 'r' and sys_input == 's') or \
         (user_input == 's' and sys_input == 'p') or \
         (user_input == 'p' and sys_input == 'r'):
        return True
    else:
        return False

round_winner = 3
user_win = 0
sys_win = 0
n_round = 1

print('Добро пожжаловать в игру Камень, Ножницы, Бумага\n'
      'Для завершения игры в любой момент введите букву Q (quit)\n'
      'Приятной игры!\n')

while True:
    if n_round > 1:
        print('-'*100)

    print('Раунд %d. Вы: %d | %d :Комп' % (n_round, user_win, sys_win))

    sys_chooise = random.choice(['r', 's', 'p'])
    user_chooise = my_input()

    if user_chooise == 'q':
        print('Игра остановленна')
        break

    winner_num = find_winner(user_chooise, sys_chooise)

    if winner_num:
        print('\nВы выиграли\n')
        user_win += 1
    elif winner_num == None:
        print('Ничья')
    else:
        print('\nВыиграл компьютер\n')
        sys_win += 1

    n_round += 1

    if user_win == round_winner:
        print('Поздравляем вы выиграли за %d раундов' % n_round)
        break
    elif sys_win == round_winner:
        print('Компьютер выиграл за %d раундов' % n_round)
        break

