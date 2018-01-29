def input_var():
    while True:
        choise = input('\nИспользовать дефолтные занчения a=1 b=2 c=3? Y or N: ')

        if choise == 'y' or choise == 'Y':
            var_a = 1
            var_b = 2
            var_c = 3
            break

        elif choise == 'n' or choise == 'N':
            var_a = int(input('Введите значение а: '))
            var_b = int(input('Введите значение b: '))
            var_c = int(input('Введите значение c: '))
            break

        else:
            print('Введите Y - если хотите использовать дефолтные значения или N - если хотите ввести свои')

    print('')
    return var_a, var_b, var_c

def has_fraction(var):
    return var - int(var) == 0

def equation(var_a, var_b, var_c):
    if var_c == 0:
        equation_1 = (var_a + var_b * var_c) ** 2
        equation_2 = 'Devision by ZERO'
        equation_3 = (var_a * var_b + 4) / (var_c - 1)
        results = [equation_1, equation_3]
        print('\nОШИБКА ПРИМЕРА 2: %s\n' % equation_2)


    elif var_c == 1:
        equation_1 = (var_a + var_b * var_c) ** 2
        equation_2 = var_a - (4 * var_b) / var_c
        equation_3 = 'Devision by ZERO'
        results = [equation_1, equation_2]
        print('\nОШИБКА ПРИМЕРА 3: %s\n' % equation_3)

    else:
        equation_1 = (var_a + var_b * var_c) ** 2
        equation_2 = var_a - (4 * var_b) / var_c
        equation_3 = (var_a * var_b + 4) / (var_c - 1)
        results = [equation_1, equation_2, equation_3]

    for i, res in enumerate(results):
        if has_fraction(res):
            print('Ответ на пример %d равен: %d' % (i + 1, res))
        else:
            print('Ответ на пример %d равен: %.3f' % (i + 1, res))

var_a, var_b, var_c = input_var()

equation(var_a, var_b, var_c)


