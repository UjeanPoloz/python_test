def my_input(n = 1):
    while True:
        try:
            var = float(input("Введите %d число для работы с ним: " % n))
        except ValueError:
            print("Алгоритм принимает только числа!\n"
                  "NOTE: Для ввода Float используйте точку (exp: 12.4\n")
        else:
            break
    return var

point_number = 10

user_number_first = my_input(1)
user_number_second = my_input(2)

length_section_first = abs(point_number - user_number_first)
length_section_second = abs(point_number - user_number_second)

if length_section_first < length_section_second:
    print('Чиcло 1 ближе к %d' % point_number)
elif length_section_second == length_section_second:
    print('Числа находятся на одном росстояние от %d' % point_number)
else:
    print('Чиcло 2 ближе к %d' % point_number)