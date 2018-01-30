def my_input(n = 1):
    while True:
        try:
            var = float(input("Введите %d число для работы с ним: " % n))
        except ValueError:
            print("Алгоритм принимает только числа!\n"
                  "NOTE: Для ввода Float используйте точку (exp: 12.4)\n")
        else:
            break
    return var

def pp_vars(var, p_num):
    if var - int(var) == 0:
        print('Чиcло %d ближе к %d' % (var, p_num))
    else:
        print('Чиcло %.3f ближе к %d' % (var, p_num))

point_number = 10.0

user_number_first = my_input(1)
user_number_second = my_input(2)

length_section_first = abs(float(point_number - user_number_first))
length_section_second = abs(float(point_number - user_number_second))

if length_section_first < length_section_second:
    pp_vars(user_number_first, point_number)

elif length_section_first > length_section_second:
    pp_vars(user_number_second, point_number)

else:
    print('Числа находятся на одном росстояние от %d' % point_number)

