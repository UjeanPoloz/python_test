def my_input():
    while True:
        try:
            var = int(input("Введите число для работы с ним: "))
        except ValueError:
            print("Алгоритм принимает только числа!\n")
        else:
            break
    return var

def multiplication_odd_num(var):
    res = 1
    odd_count = 0

    if var == 0:
        print("Ноль чётное число")
        res = 0

    num_list = list(str(var))

    for number in num_list:
        if not int(number) %2 == 0:
            res *= int(number)
            odd_count += 1

        if odd_count == 0:
            res = 0

    print("\nПроизведение нечетных цифр введенного целого числа равно: %d" % res)

multiplication_odd_num(my_input())



