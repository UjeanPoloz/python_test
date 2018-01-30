import random

def pretty_print_matrix(matrix, sorted=False):
    if sorted:
        print('\n---Sorted Matrix---\n')
    else:
        print('\n---Matrix---\n')


    for row in matrix:
        for elem in row:
            print('%d' % elem, end='\t')
        print()
    print()

def sort_matrix(group):
    group = list(zip(*group[::-1]))

    for ind in range(len(group)):
        group[ind] = list(group[ind])
        if ind %2 == 0:
            group[ind].sort(reverse=True)
        else:
            group[ind].sort()

    group = list(zip(*group[::1]))
    return group

matrix_columns = 5
matrix_rows = 3
low_bound = -5
hight_bound = abs(low_bound)

matrix = [[random.randint(low_bound, hight_bound) for i in range(matrix_columns)] \
          for ii in range(matrix_rows)]


pretty_print_matrix(matrix)

pretty_print_matrix(sort_matrix(matrix), True)