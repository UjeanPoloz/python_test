def fibonchi_row(number):
    if number == 1 or number == 2:
        return 1
    else:
        return fibonchi_row(number - 1) + fibonchi_row(number - 2)

def my_input():
    while True:
        try:
            var = int(input("Введите номер числа из ряда Фибоначи для просчета сумм всех чисел до этого числа: "))
        except ValueError:
            print("Алгоритм принимает только числа!\n")
        else:
            break
    return var

summ_fibonachi = 0

user_input = my_input()

for i in range(1,user_input+1):
    summ_fibonachi += fibonchi_row(i)

print('Сумма первых %d чисел ряда Фибоначчи равна: %d' % (user_input, summ_fibonachi))