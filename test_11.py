import random

def pretty_print_matrix(matrix, n=0):
    if n == 0:
        print('\n---Matrix---\n')
    else:
        print('\n---Sorted Matrix---\n')

    for row in matrix:
        for elem in row:
            print('%d' % elem, end='\t')
        print()
    print()

# def sort_matrix(group):
#     copy_group = group
#     sorted_group = [[i for i in range(rows)] \
#                     for ii in range(columns)]
#     new_row = []
#
#     print(sorted_group)
#     # group.sort(reverse=False, key=lambda elem: elem[1])
#     for ind_rows in range(len(copy_group)):
#         for ind_var in range(len(group[ind_rows])):
#             new_row.append(group[ind_rows][ind_var])
#         print(new_row)

def sorted_matrix(group):
    group = list(tuple(zip(*group[::-1])))

    for ind in range(len(group)):
        group[ind] = list(group[ind])
        if ind %2 == 0:
            group[ind].sort(reverse=True)
        else:
            group[ind].sort()

    group = list(tuple(zip(*group[::1])))
    return group

matrix_columns = 5
matrix_rows = 3
low_bound = -5
hight_bound = abs(low_bound)

matrix = [[random.randint(low_bound, hight_bound) for i in range(matrix_columns)] \
          for ii in range(matrix_rows)]


pretty_print_matrix(matrix)

pretty_print_matrix(sorted_matrix(matrix), n=1)
