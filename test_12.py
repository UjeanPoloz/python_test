import random

def pretty_print_lit(lst, n):
    print('---- Список упражнения для %d учеников ----' % n)
    for i in range(len(lst)):
        print('Упражнение %d: \t%s' % (i+1, lst[i]))

def exercise_generator(student_count, first_number, last_number):
    lst_exr = ['' for _ in range(student_count)]
    lst_var = [_ for _ in range(first_number,last_number+1)]

    for ind in range(len(lst_exr)):
        while True:
            var_one = random.choice(lst_var)
            var_two = random.choice(lst_var)
            exr = str(var_one) + ' * ' + str(var_two)
            if is_not_duplicate(exr, lst_exr):
                lst_exr[ind] = exr
                break

    return lst_exr

def is_not_duplicate(exr, lst_exr):
    lst_vars = exr.split(' * ')
    test_one = str(lst_vars[0]) + ' * ' + str(lst_vars[1])
    test_two = str(lst_vars[1]) + ' * ' + str(lst_vars[0])

    if not test_one in lst_exr:
        return True

    elif not test_two in lst_exr:
        return True

    else:
        return False


student_count = 15
first_number = 2
last_number = 9

pretty_print_lit(exercise_generator(student_count,first_number,last_number), student_count)