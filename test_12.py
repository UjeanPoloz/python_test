import random

def pretty_print_lit(lst, n):
    print('---- Список упражнения для %d учеников ----' % n)
    for i in range(len(lst)):
        print('Упражнение %d: \t%s' % (i+1, lst[i]))

def exercise_generator(student_count, first_number, last_number):
    lst_exr = ['']*student_count
    lst_var = [i for i in range(first_number,last_number+1)]

    ind = 0

    # for ind in range(student_count):
    #     while True:
    #         var_one = random.choice(lst_var)
    #         var_two = random.choice(lst_var)
    #         exr = str(var_one) + ' * ' + str(var_two)
    #         if is_not_duplicate(exr, lst_exr):
    #             lst_exr[ind] = exr
    #             break

    while ind != student_count:
        var_one = random.choice(lst_var)
        var_two = random.choice(lst_var)
        exr = str(var_one) + ' * ' + str(var_two)

        if is_not_duplicate(exr, lst_exr):
                lst_exr[ind] = exr
                ind += 1

    return lst_exr

def is_not_duplicate(exr, lst_exr):
    return (exr not in lst_exr) and (exr[::-1] not in lst_exr)


student_count = 15
first_number = 2
last_number = 9

pretty_print_lit(exercise_generator(student_count,first_number,last_number), student_count)