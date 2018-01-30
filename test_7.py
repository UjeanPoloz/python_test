def fiboncсi_row(number):
    if number == 1 or number == 2:
        return 1
    else:
        return fiboncсi_row(number - 1) + fiboncсi_row(number - 2)

def my_input():
    while True:
        try:
            var = int(input("Введите номер числа из ряда Фибоначи для просчета сумм всех чисел до этого числа: "))
        except ValueError:
            print("Алгоритм принимает только числа!\n")
        else:
            break
    return var

summ_fibonacсi = 0

user_input = my_input()

summ_fibonacсi = sum([fiboncсi_row(i) for i in range(1,user_input+1)])

print('\nСумма первых %d чисел ряда Фибоначчи равна: %d' % (user_input, summ_fibonacсi))